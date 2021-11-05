import datetime
import json
import os
import sys
import ast
import urllib2
import urllib, urllib3
import zipfile
import base64
from email.mime.application import MIMEApplication
from email.mime.base import MIMEBase
from email import encoders

triggerEmail = ""
senderMail = ""
senderPassword = ""

triggerEmail = sys.argv[1]
senderMail = sys.argv[2]
senderPassword = sys.argv[3]
receiverEmails = sys.argv[4]
platform = sys.argv[5]
enviornment = sys.argv[6]
ciJobURL = os.environ['CI_JOB_URL']
ciDockerToken = os.environ['CI_DOCKER_TOKEN']
ciProjectId = os.environ['CI_PROJECT_ID']


def getCurrentJobId():
    return ciJobURL.split("jobs/")[1]

def getJobDuration():
    url = "https://code.siemens.com/api/v4/projects/" + ciProjectId + "/jobs/" + getCurrentJobId() + ""
    headers = {"PRIVATE-TOKEN": ciDockerToken}
    request = urllib2.Request(url, headers=headers)
    contents = urllib2.urlopen(request).read()
    data = json.loads(contents)
    d = str(data['duration'])
    t = d.split(".")[0]
    duration = str(datetime.timedelta(seconds=int(t)))
    return duration

def getStartTime():
    url = "https://code.siemens.com/api/v4/projects/" + ciProjectId + "/jobs/" + getCurrentJobId() + ""
    headers = {"PRIVATE-TOKEN": ciDockerToken}
    request = urllib2.Request(url, headers=headers)
    contents = urllib2.urlopen(request).read()
    data = json.loads(contents)
    startedAt = str(data['started_at'])
    return startedAt

def getEndTime():
    url = "https://code.siemens.com/api/v4/projects/" + ciProjectId + "/jobs/" + getCurrentJobId() + ""
    headers = {"PRIVATE-TOKEN": ciDockerToken}
    request = urllib2.Request(url, headers=headers)
    contents = urllib2.urlopen(request).read()
    data = json.loads(contents)
    endTime = str(data['finished_at'])
    return endTime

def getArtifactsExpiry():
    url = "https://code.siemens.com/api/v4/projects/" + ciProjectId + "/jobs/" + getCurrentJobId() + ""
    headers = {"PRIVATE-TOKEN": ciDockerToken}
    request = urllib2.Request(url, headers=headers)
    contents = urllib2.urlopen(request).read()
    data = json.loads(contents)
    expiryAt = str(data['artifacts_expire_at'])
    return expiryAt

def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file),
                       os.path.relpath(os.path.join(root, file),
                                       os.path.join(path, '..')))

def decryptPassword():
    base64_bytes = senderPassword.encode("ascii")
    sample_string_bytes = base64.b64decode(base64_bytes)
    decodedPass = sample_string_bytes.decode("ascii")
    return  decodedPass


def parseHTMLFile(pathFile):
    with open(pathFile, 'r') as f:
        html_string = f.read()
        return html_string

def sendEmail() :
    from smtplib import SMTP_SSL
    from smtplib import SMTP
    import ssl
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    from datetime import date

    screenshots_dir = "reports/screenshots"
    startedAt = getStartTime()
    endedAt = getEndTime()
    duration = getJobDuration()
    expiryAt = getArtifactsExpiry()

    today = date.today()
    to_email = ast.literal_eval(receiverEmails)

    from_email = senderMail
    subject = 'Date: ' + str(today) + ' - Automated Execution Report for '+platform+' '+enviornment+' !'
    message = MIMEMultipart()
    message['Subject'] = subject
    message['From'] = from_email
    message['To'] = ", ".join(to_email)
    htmlbody = '''<html>
<body>
<p>Hello All,</p>
<p>Please go through summary and detailed execution report respectively</p>
<div>
<table style="height: 146px; width: 730px; border-color: #000000; float: left;" border="1">
<tbody>
<tr>
<td style="width: 165px; background-color: #009999 color: white;">&nbsp; Job URL</td>
<td style="width: 800px;">&nbsp;&nbsp;<a href="''' + ciJobURL + '''" target="_blank" rel="noopener">''' + ciJobURL + '''</a></td>
</tr>
<tr>
<td style="width: 165px; background-color: #009999 color: white;">&nbsp; Started At</td>
<td style="width: 800px;">&nbsp; ''' + startedAt + '''</td>
</tr>
<tr>
<td style="width: 165px; background-color: #009999 color: white;">&nbsp; Duration</td>
<td style="width: 800px;">&nbsp;&nbsp;''' + duration + '''</td>
</tr>
<tr>
<td style="width: 165px; background-color: #009999 color: white;">&nbsp; Artifacts Link</td>
<td style="width: 800px;">&nbsp; &nbsp;<a href="''' + ciJobURL + '''/artifacts/download" target="_blank" rel="noopener">''' + ciJobURL + '''/artifacts/download</a></td>
</tr>
<tr>
<td style="width: 165px; background-color: #009999 color: white;">&nbsp; Artifacts Expires At</td>
<td style="width: 800px;">&nbsp;&nbsp; 5 days later Started At</td>
</tr>
</tbody>
</table>
</div>
</body>
 </html>'''

    spacehtml = '''<html>
                   <body>
                   <p>&nbsp;</p>
                   </body>
                   </html>'''
    message.attach(MIMEText(htmlbody + spacehtml + parseHTMLFile('reports/reportSummary.html') + parseHTMLFile('reports/report.html') , "html", "utf-8"))

    try:
        files = os.listdir(screenshots_dir)
        for f in files:  # add files to the message
            file_path = os.path.join(screenshots_dir, f)
            attachment = MIMEApplication(open(file_path, "rb").read())
            attachment.add_header('Content-Disposition', 'attachment', filename=f)
            message.attach(attachment)

    except Exception as e:
        print('Oh ! Seems there are no failed UI cases, hence screenshots not attached to email.')

    server = SMTP('pnsmtp.net.plm.eds.com', 25)
    server.starttls()
    server.login(from_email, decryptPassword())
    server.sendmail(from_email, to_email, message.as_string())
    server.quit()


if (triggerEmail.__eq__('true')) :
    print('Sender is --> ' + senderMail)
    print('Receivers list is --> ')
    print(receiverEmails)
    print('Sending email....')
    sendEmail()
    print('Email sent to above receivers....')


from pywinauto import application
import time

app = application.Application()
app.start("Notepad.exe")
time.sleep(5)
# app.Notepad.edit
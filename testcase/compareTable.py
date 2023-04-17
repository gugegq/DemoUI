import pandas as pd

dir_path="C://Users//qiagu42q//Downloads//"
# 读取多个表格数据
df1 = pd.read_excel(dir_path+'dextest.xlsx')
df2 = pd.read_excel(dir_path+'QAC.xlsx')
df3 = pd.read_excel(dir_path+'UAT.xlsx')

# 按照指定列进行数据合并
merged_df = pd.merge(df1, df2, on=['col1', 'col2', 'col3'])

# 选择需要对比的列，并比较数据差异
diff_df = merged_df[merged_df['col4_x'] != merged_df['col4_y']]

# 保存比较结果到新表格
diff_df.to_excel(dir_path+'diff_table.xlsx', index=False)
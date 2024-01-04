import pandas as pd
import sys
#比较之前的country和现在新引入的差距
#比较国家和合作伙伴之间的关系

# 添加项目根目录到 Python 路径
project_root = 'f:\\zyy_wto\\webgis'
if project_root not in sys.path:
    sys.path.append(project_root)

# 读取 Excel 文件
df = pd.read_excel('F:/zyy_wto/data/Commercial_services_export.xlsx')
df.fillna(0, inplace=True)  # 将所有的 nan 值替换为 0

# 读取 Excel 文件
df2 = pd.read_excel('F:/zyy_wto/data/WtoData_import.xlsx')
df2.fillna(0, inplace=True)  # 将所有的 nan 值替换为 0

df['Partner Economy'] = df['Partner Economy'].str.lower().str.strip()
df2['Reporting Economy'] = df2['Reporting Economy'].str.lower().str.strip()
df2['Partner Economy'] = df2['Partner Economy'].str.lower().str.strip()

# 得到不重复的国家列表和合作伙伴列表
unique_countries = df2['Reporting Economy'].unique()
unique_partners = df['Partner Economy'].unique()

print(len(unique_countries))
print(len(unique_partners))

# 判断每个国家是否都包含在合作伙伴列表中
countries_in_partners = all(country in unique_partners for country in unique_countries)
# 输出结果
if countries_in_partners:
    print("每个国家都包含在合作伙伴列表中。")
else:
    print("有国家不包含在合作伙伴列表中。")
    print

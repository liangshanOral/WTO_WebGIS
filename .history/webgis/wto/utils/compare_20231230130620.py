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
print(df.columns)

# 转换为小写并去除额外的空格
df['Reporting Economy'] = df['Reporting Economy'].str.lower().str.strip()
df['Partner Economy'] = df['Partner Economy'].str.lower().str.strip()

# 得到不重复的国家列表和合作伙伴列表
unique_countries = df['Reporting Economy'].unique()
unique_partners = df['Partner Economy'].unique()

print(len(unique_countries))
print(len(unique_partners))

# 比较两个列表的差异
countries_diff = set(unique_countries) - set(unique_partners)
partners_diff = set(unique_partners) - set(unique_countries)

# 显示差异
print("不同的国家:", countries_diff)
print("不同的合作伙伴:", partners_diff)

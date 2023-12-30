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

unique_countries = df['Reporting Economy'].unique()
unique_partners = df['Partner Economy'].unique()

countries_diff = set(unique_countries) - set(unique_partners)
partners_diff = set(unique_partners) - set(unique_countries)

print("不同的国家:", countries_diff)
print("不同的合作伙伴:", partners_diff)


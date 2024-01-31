import os
import django
import sys
import pandas as pd

# 添加项目根目录到 Python 路径
project_root = 'f:\\zyy_wto\\webgis'
if project_root not in sys.path:
    sys.path.append(project_root)
# 设置 Django 环境
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webgis.settings')
django.setup()

# 现在可以导入 Django 模型
from wto.models import MFN_a, Country_L

# 读取 Excel 文件
df = pd.read_excel('F:/zyy_wto/data/MFN-all_products.xlsx')
df.fillna(0, inplace=True)  # 将所有的 nan 值替换为 0

# 获取年份列名
year_columns = [2022,2021,2020,2019,2018,2017,2016,2015,2014,2013,2012,2011,2010,2009,2008,2007,2006,2005]

for index, row in df.iterrows():
    # 提取数据
    reporting_country_name = row['Reporting Economy']

    # 根据国家名称和产品/部门名称获取相应的对象或创建新对象
    reporting_country, _ = Country_L.objects.get_or_create(name=reporting_country_name)
   
    for year_col in year_columns:
        year = year_col
        value_y = row[year_col]

        # 创建或更新 TradeYearData 对象
        MFN_a.objects.create(
            reporting_country=reporting_country,
            year=year,
            MFN_value=value_y,
        )
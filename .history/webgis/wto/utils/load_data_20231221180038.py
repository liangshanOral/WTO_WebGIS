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
from wto.models import TradeYearData, Country, ProductSector

# 读取 Excel 文件
df = pd.read_excel('data/WtoData_export.xlsx')

# 获取年份列名
year_columns = [2022,]

# 遍历 DataFrame 的行
for index, row in df.iterrows():
    # 从行中提取数据
    reporting_country_name = row['Reporting Economy']
    product_sector_name = row['Product/Sector']
    partner_country_name = row['Partner Economy']

    # 根据国家名称和产品/部门名称获取相应的对象或创建新对象
    reporting_country, _ = Country.objects.get_or_create(name=reporting_country_name)
    product_sector, _ = ProductSector.objects.get_or_create(name=product_sector_name)
    partner_country, _ = Country.objects.get_or_create(name=partner_country_name)

    for year_col in year_columns:
        year = int(year_col)
        export_value_y = row[year_col]
        # import_value_y = row[year_col]  # 如果你也需要导入值

        # 创建或更新 TradeYearData 对象
        TradeYearData.objects.create(
            reporting_country=reporting_country,
            product_sector=product_sector,
            partner_country=partner_country,
            year=year,
            export_value_y=export_value_y,
            # import_value_y=import_value_y,
        )
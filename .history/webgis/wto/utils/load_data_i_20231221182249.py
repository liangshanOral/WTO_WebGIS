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
df = pd.read_excel('F:/zyy_wto/data/WtoData_export.xlsx')
df.fillna(0, inplace=True)  # 将所有的 nan 值替换为 0

# 获取年份列名
year_columns = [2022,2021,2020,2019,2018,2017,2016,2015]

for index, row in df.iterrows():
    # 提取数据
    reporting_country_name = row['Reporting Economy']
    product_sector_name = row['Product/Sector']
    partner_country_name = row['Partner Economy']

    for year_col in year_columns:
        year = int(year_col)
        import_value_y = row[year_col]

        # 更新 TradeYearData 实例
        try:
            trade_data = TradeYearData.objects.get(
                reporting_country__name=reporting_country_name,
                product_sector__name=product_sector_name,
                partner_country__name=partner_country_name,
                year=year
            )
            trade_data.import_value_y = import_value_y
            trade_data.save()
        except TradeYearData.DoesNotExist:
            # 处理记录不存在的情况，如跳过或创建新记录
            pass
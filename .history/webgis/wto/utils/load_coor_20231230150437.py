import os
import django
import pandas as pd
import sys

# 添加项目根目录到 Python 路径
project_root = 'f:\\zyy_wto\\webgis'
if project_root not in sys.path:
    sys.path.append(project_root)
# 设置 Django 环境
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webgis.settings')
django.setup()

from wto.models import Country_L, ProductSector_L, CommercialData_E

# 读取包含国家和经纬度信息的 Excel 文件
df = pd.read_excel("F:\zyy_wto\data\Commercial_services_export_with_coordinates.xlsx")

# 遍历 DataFrame，更新数据库中的经纬度信息
for index, row in df.iterrows():
    reporting_country_name = row['Reporting Economy']  # 假设 'Country' 是国家列的标题
    latitude = row['Latitude']     # 假设 'Latitude' 是经度列的标题
    longitude = row['Longitude']   # 假设 'Longitude' 是纬度列的标题
    product_sector_name = row['Product/Sector']
    partner_country_name = row['Partner Economy']

    # 根据国家名称和产品/部门名称获取相应的对象或创建新对象
    reporting_country, _ = Country_L.objects.get_or_create(name=reporting_country_name)
    product_sector, _ = ProductSector_L.objects.get_or_create(name=product_sector_name)
    partner_country, _ = Country_L.objects.get_or_create(name=partner_country_name)

    # 更新经纬度信息
    partner_country.latitude = latitude
    partner_country.longitude = longitude
    for year_col in year_columns:
    year = int(year_col)
    import_value = row[year_col]
    # import_value_y = row[year_col]  # 如果你也需要导入值

    # 创建或更新 TradeYearData 对象
    CommercialData_I.objects.create(
        reporting_country=reporting_country,
        product_sector=product_sector,
        partner_country=partner_country,
        year=year,
        import_value=import_value,
        # import_value_y=import_value_y,
    )

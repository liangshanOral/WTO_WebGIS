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

from wto.models import Country_L

# 读取包含国家和经纬度信息的 Excel 文件
df = pd.read_excel("F:\zyy_wto\data\Commercial_services_export_with_coordinates.xlsx")

# 遍历 DataFrame，更新数据库中的经纬度信息
for index, row in df.iterrows():
    country_name = row['Partner Economy']  # 假设 'Country' 是国家列的标题
    latitude = row['Latitude']     # 假设 'Latitude' 是经度列的标题
    longitude = row['Longitude']   # 假设 'Longitude' 是纬度列的标题
    product_sector_name = row['Product/Sector']
    partner_country_name = row['Partner Economy']
    
    # 获取或创建国家对象
    country, created = Country_L.objects.get_or_create(name=country_name)

    # 更新经纬度信息
    country.latitude = latitude
    country.longitude = longitude
    country.save()

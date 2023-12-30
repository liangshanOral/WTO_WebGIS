import pandas as pd
from wto.models import Country_L


# 读取包含国家和经纬度信息的 Excel 文件
df = pd.read_excel("your_excel_file.xlsx")

# 遍历 DataFrame，更新数据库中的经纬度信息
for index, row in df.iterrows():
    country_name = row['Country']  # 假设 'Country' 是国家列的标题
    latitude = row['Latitude']     # 假设 'Latitude' 是经度列的标题
    longitude = row['Longitude']   # 假设 'Longitude' 是纬度列的标题

    # 获取或创建国家对象
    country, created = Country.objects.get_or_create(name=country_name)

    # 更新经纬度信息
    country.latitude = latitude
    country.longitude = longitude
    country.save()

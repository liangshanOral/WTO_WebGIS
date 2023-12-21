import csv 
from wto.models import TradeYearData, Country, ProductSector

with open('data/WtoData_export.xlsx') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        Country.name = row['Reporting Economy']
        ProductSector.name = row['Product/Sector']
        partner_country_name = row['Partner Economy']
        TradeYearData.year = int(row['Year'])  # 根据实际列名提取年份数据

         # 创建TradeYearData实例并保存到数据库
        trade_year_data = TradeYearData.objects.create(
            reporting_country=reporting_country,
            product_sector=product_sector,
            partner_country=partner_country,
            year=year,
            export_value_y=row['Export Value'],  # 根据实际列名提取出口值
            import_value_y=row['Import Value'],  # 根据实际列名提取进口值
        )
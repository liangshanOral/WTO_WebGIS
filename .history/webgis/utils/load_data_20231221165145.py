import csv 
from wto.models import TradeYearData, Country, ProductSector

with open('data/WtoData_export.xlsx') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        Country.name = row['Reporting Economy']
        ProductSector.name = row['Product/Sector']
        partner_country_name = row['Partner Economy']
        TradeYearData.year = int(row['Year'])  # 根据实际列名提取年份数据
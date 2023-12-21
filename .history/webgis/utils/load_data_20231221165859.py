import csv 
from wto.models import TradeYearData, Country, ProductSector

with open('data/WtoData_export.xlsx') as csv_file:
    csv_reader = csv.DictReader(csv_file)

     # 获取年份列名
    year_columns = [col for col in csv_reader.fieldnames if col.isdigit()]

    for row in csv_reader:
         # 从CSV行中提取数据
        reporting_country_name = row['Reporting Economy']
        product_sector_name = row['Product/Sector']
        partner_country_name = row['Partner Economy']
        
        for year_col in year_columns:
            year = int(year_col)
            export_value_y = row[year_col]
            import_value_y = row[year_col]

             trade_year_data = TradeYearData.objects.create(
                reporting_country=reporting_country_name,
                product_sector=product_sector_name,
                partner_country=partner_country_name,
                year=year,
                export_value_y=export_value_y,
                import_value_y=import_value_y,
            )

        year = int(row['Year'])  # 根据实际列名提取年份数据

        # 根据国家名称和产品/部门名称获取相应的对象或创建新对象
        reporting_country, _ = Country.objects.get_or_create(name=reporting_country_name)
        product_sector, _ = ProductSector.objects.get_or_create(name=product_sector_name)
        partner_country, _ = Country.objects.get_or_create(name=partner_country_name)

        # 创建TradeYearData实例并保存到数据库
        trade_year_data = TradeYearData.objects.create(
            reporting_country=reporting_country,
            product_sector=product_sector,
            partner_country=partner_country,
            year=year,
            export_value_y=row['Export Value'],  # 根据实际列名提取出口值
            import_value_y=row['Import Value'],  # 根据实际列名提取进口值
        )
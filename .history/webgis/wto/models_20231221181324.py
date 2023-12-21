from django.db import models

# Create your models here.
class Country(models.Model):
    #code = models.CharField(max_length=3, unique=True)  # If a code is available
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name

class ProductSector(models.Model):
    #code = models.CharField(max_length=10)  # Extract the code if present, e.g., 'TO'
    name = models.CharField(max_length=255)  # The full description

    def __str__(self):
        return self.name
    
class TradeYearData(models.Model):
    reporting_country = models.ForeignKey(Country, related_name='reporting_year_country', on_delete=models.CASCADE)
    partner_country = models.ForeignKey(Country, related_name='partner_country', on_delete=models.CASCADE)
    product_sector = models.ForeignKey(ProductSector, on_delete=models.CASCADE)
    year = models.IntegerField()
    export_value_y = models.DecimalField(max_digits=14, decimal_places=2,null=True, blank=True)
    import_value_y = models.DecimalField(max_digits=14, decimal_places=2,null=True, blank=True)

class TradeQuarterData(models.Model):
    reporting_country = models.ForeignKey(Country, related_name='reporting_quarter_country', on_delete=models.CASCADE)
    #partner_country = models.ForeignKey(Country, related_name='partner_country', on_delete=models.CASCADE,default="World")
    #product_sector = models.ForeignKey(ProductSector, on_delete=models.CASCADE,default="SI3_AGG - TO - Total merchandise")
    Quarter = models.IntegerField()
    export_value_q = models.DecimalField(max_digits=14, decimal_places=2,null=True, blank=True)
    import_value_q = models.DecimalField(max_digits=14, decimal_places=2,null=True, blank=True)

class TradeMonthData(models.Model):
    reporting_country = models.ForeignKey(Country, related_name='reporting_month_country', on_delete=models.CASCADE)
    #partner_country = models.ForeignKey(Country, related_name='partner_country', on_delete=models.CASCADE,default="World")
    #product_sector = models.ForeignKey(ProductSector, on_delete=models.CASCADE,default="SI3_AGG - TO - Total merchandise")
    export_value_m = models.DecimalField(max_digits=14, decimal_places=2,null=True, blank=True)
    import_value_m = models.DecimalField(max_digits=14, decimal_places=2)

class TradeYearIndex(models.Model):
    reporting_country = models.ForeignKey(Country, related_name='reporting_index_country', on_delete=models.CASCADE)
    #partner_country = models.ForeignKey(Country, related_name='partner_country', on_delete=models.CASCADE,default="World")
    #product_sector = models.ForeignKey(ProductSector, on_delete=models.CASCADE,default="SI3_AGG - TO - Total merchandise")
    year = models.IntegerField()
    export_value_i = models.DecimalField(max_digits=14, decimal_places=2)
    import_value_i = models.DecimalField(max_digits=14, decimal_places=2)

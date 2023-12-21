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
    
class TradeData(models.Model):
    reporting_country = models.ForeignKey(Country, related_name='reporting_country', on_delete=models.CASCADE)
    partner_country = models.ForeignKey(Country, related_name='partner_country', on_delete=models.CASCADE)
    product_sector = models.ForeignKey(ProductSector, on_delete=models.CASCADE)
    year = models.IntegerField()
    export_value_y = models.DecimalField(max_digits=14, decimal_places=2)
    import_value_y = models.DecimalField(max_digits=14, decimal_places=2)

class TradeQu

    export_value_q = models.DecimalField(max_digits=14, decimal_places=2)
    import_value_q = models.DecimalField(max_digits=14, decimal_places=2)
    export_value_m = models.DecimalField(max_digits=14, decimal_places=2)
    import_value_m = models.DecimalField(max_digits=14, decimal_places=2)
    export_value_i = models.DecimalField(max_digits=14, decimal_places=2)
    import_value_i = models.DecimalField(max_digits=14, decimal_places=2)

from django.contrib import admin
from .models import Country, ProductSector, TradeYearData_E, TradeYearData_I, TradeQuarterData_E, TradeQuarterData_I, TradeMonthData_E, TradeMonthData_I, TradeYearIndex_E, TradeYearIndex_I, Country_L, ProductSector_L, 

# Register your models here.
admin.site.register(Country)
admin.site.register(ProductSector)
admin.site.register(TradeYearData_E)
admin.site.register(TradeYearData_I)
admin.site.register(TradeQuarterData_E)
admin.site.register(TradeQuarterData_I)
admin.site.register(TradeMonthData_E)
admin.site.register(TradeMonthData_I)
admin.site.register(TradeYearIndex_E)
admin.site.register(TradeYearIndex_I)

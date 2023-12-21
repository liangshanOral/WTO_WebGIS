from django.contrib import admin
from .models import Country, ProductSector, TradeYearData_E, TradeYearData_I, TradeQuarterData_E, TradeQuarterData_I, TradeMonthData_E, TradeMonthData_I, TradeYearIndex_E, TradeYearIndex_I

# Register your models here.
admin.site.register(Country)
admin.site.register(ProductSector)
admin.site.register(TradeYearData)
admin.site.register(TradeQuarterData)
admin.site.register(TradeMonthData)
admin.site.register(TradeYearIndex)
'''
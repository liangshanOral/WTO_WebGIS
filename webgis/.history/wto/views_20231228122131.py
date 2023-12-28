from django.shortcuts import render
from django.http import JsonResponse
from .models import Country, ProductSector, TradeYearData_E

def get_country_product_data(request):
    countries = Country.objects.values_list('name', flat=True)
    products = ProductSector.objects.values_list('name', flat=True)

    return JsonResponse({'countries': list(countries), 'products': list(products)})

def echarts_data(request):
    # 在这里处理前端传递的参数，查询数据库，获取相应的数据
    # 示例：假设你的模型是 TradeYearData_E
    selected_country = request.GET.getlist('country', '')
    selected_product = request.GET.getlist('product', '')

    #queryset = TradeYearData_E.objects.filter(reporting_country__name=selected_country, product_sector__name=selected_product)
    # 查询每个国家下选择的品类的加总数据
    queryset = TradeYearData_E.objects.filter(
        reporting_country__name=selected_country,
        product_sector__name__in=selected_product
    ).values('product_sector__name').annotate(total_export=Sum('export_value_y'))
    
    data = [{'year': entry.year, 'export_value_y': entry.export_value_y} for entry in queryset]

    return JsonResponse({'data': data})

def index(request):
    return render(request, 'index.html') #相对于templates进行查找

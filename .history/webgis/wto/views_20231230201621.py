from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Sum,Q
from .models import Country, ProductSector, TradeYearData_E,ProductSector_L

def get_country_product_data(request):
    countries = Country.objects.values_list('name', flat=True)
    products = ProductSector.objects.values_list('name', flat=True)

    return JsonResponse({'countries': list(countries), 'products': list(products)})

def get_flow_data(request):
    products=ProductSector_L.objects.values_list('name',flat=True)
    return JsonResponse({'products': list(products)})

def echarts_data(request):
    # 在这里处理前端传递的参数，查询数据库，获取相应的数据
    # 示例：假设你的模型是 TradeYearData_E
    # 将传递的字符串参数拆分成列表
    selected_country = [country.strip() for country in request.GET.get('country', '').split(',') if country.strip()]
    selected_product = [product.strip() for product in request.GET.get('product', '').split(',') if product.strip()]

    print(selected_country, selected_product)

    # 使用 Q 对象构建动态的查询条件
    query = Q()
    for country in selected_country:
        for product in selected_product:
            query |= Q(reporting_country__name=country, product_sector__name=product)
    
    # 查询数据库
    queryset = TradeYearData_E.objects.filter(query)
    print(queryset)
    # 将 TradeYearData_E 对象转为字典
    data = [{'year': entry.year, 'country': entry.reporting_country.name, 'product': entry.product_sector.name, 'export_value_y': entry.export_value_y} for entry in queryset]
    return JsonResponse({'data': data})
def echarts_data(request):
    # 在这里处理前端传递的参数，查询数据库，获取相应的数据
    # 示例：假设你的模型是 TradeYearData_E
    # 将传递的字符串参数拆分成列表
    selected_country = [country.strip() for country in request.GET.get('country', '').split(',') if country.strip()]
    selected_product = [product.strip() for product in request.GET.get('product', '').split(',') if product.strip()]

    print(selected_country, selected_product)

    # 使用 Q 对象构建动态的查询条件
    query = Q()
    for country in selected_country:
        for product in selected_product:
            query |= Q(reporting_country__name=country, product_sector__name=product)
    
    # 查询数据库
    queryset = TradeYearData_E.objects.filter(query)
    print(queryset)
    # 将 TradeYearData_E 对象转为字典
    data = [{'year': entry.year, 'country': entry.reporting_country.name, 'product': entry.product_sector.name, 'export_value_y': entry.export_value_y} for entry in queryset]
    return JsonResponse({'data': data})

def index(request):
    return render(request, 'index.html') #相对于templates进行查找

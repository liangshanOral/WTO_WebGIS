from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Sum,Q
from .models import Country, ProductSector, TradeYearData_E

def get_country_product_data(request):
    countries = Country.objects.values_list('name', flat=True)
    products = ProductSector.objects.values_list('name', flat=True)

    return JsonResponse({'countries': list(countries), 'products': list(products)})

def echarts_data(request):
    # 在这里处理前端传递的参数，查询数据库，获取相应的数据
    # 示例：假设你的模型是 TradeYearData_E
    # 将传递的字符串参数拆分成列表
    selected_country = request.GET.get('country', '').split(',')
    selected_product = request.GET.get('product', '').split(',')

    # 处理产品参数，确保每个产品名称被引号包裹
    #selected_product = [f'"{product.strip()}"' for product in selected_product]

    print(selected_country, selected_product)
    # 处理产品参数，确保每个产品名称被单引号包裹
    #selected_country = [f'{country.strip()}' for country in selected_country[0].split(',')]
    #selected_product = [f'{product.strip()}' for product in selected_product[0].split(',')]
    #print(selected_country,selected_product)
    
   # 使用 Q 对象构建动态的查询条件
    query = Q()
    for country in selected_country:
        for product in selected_products:
            query |= Q(reporting_country__name=country, product_sector__name=product)

    # 查询数据库
    queryset = TradeYearData_E.objects.filter(query)
    data = list(queryset)
    return JsonResponse({'data': data})

def index(request):
    return render(request, 'index.html') #相对于templates进行查找

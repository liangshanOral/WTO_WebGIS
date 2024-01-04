from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Sum,Q
from .models import Country, ProductSector, TradeYearData_E,ProductSector_L,CommercialData_E

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

def echarts_flow_data(request):
    # 在这里处理前端传递的参数，查询数据库，获取相应的数据
    # 将传递的字符串参数拆分成列表
    selected_time = [time.strip() for time in request.GET.get('time', '').split(',') if time.strip()]
    selected_product = [product.strip() for product in request.GET.get('product', '').split(',') if product.strip()]

    print(selected_time, selected_product)

    # 使用 Q 对象构建动态的查询条件
    query = Q()
    for time in selected_time:
        for product in selected_product:
            query |= Q(year=time, product_sector__name=product, export_value__gt=2)
    
    # 查询数据库
    queryset = CommercialData_E.objects.filter(query)
    #print(queryset)

    # 构建节点和边的列表
    nodes = set()
    edges = []

    for entry in queryset:
        reporting_country = entry.reporting_country.name
        partner_country = entry.partner_country.name
        export_value = entry.export_value

        # 添加节点及经纬度信息
        reporting_country_node = {
            'name': reporting_country,
            'latitude': entry.reporting_country.latitude,
            'longitude': entry.reporting_country.longitude,
        }
        nodes.add(reporting_country_node)

        partner_country_node = {
            'name': partner_country,
            'latitude': entry.partner_country.latitude,
            'longitude': entry.partner_country.longitude,
        }
        nodes.append(partner_country_node)

        # 添加边
        edges.append({
            'source': reporting_country_node,
            'target': partner_country_node,
            'value': export_value,
        })

    # 过滤掉值为 None 或 undefined 的节点
    valid_nodes = {k: v for k, v in nodes.items() if v is not None}

    # 将节点的值转换为列表
    nodes_list = list(valid_nodes.values())

    # 将节点和边的列表传递给前端
    data = {
        'nodes': nodes_list,
        'edges': edges,
    }

    return JsonResponse(data)

def index(request):
    return render(request, 'index.html') #相对于templates进行查找

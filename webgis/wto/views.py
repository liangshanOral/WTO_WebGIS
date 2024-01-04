from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Sum,Q
from .models import Country, Country_L, ProductSector, ProductSector_MFN, ProductSector_L, TradeMonthData_E, TradeMonthData_I, TradeQuarterData_E, TradeQuarterData_I, TradeYearData_E, TradeYearData_I, TradeYearIndex_E, TradeYearIndex_I, CommercialData_E_Individual, CommercialData_I_Individual, MFN_a, MFN_b, TradeYearData_E_Individual, TradeYearData_I_Individual

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

def echarts_data_import(request):
    selected_country = [country.strip() for country in request.GET.get('country', '').split(',') if country.strip()]
    selected_product = [product.strip() for product in request.GET.get('product', '').split(',') if product.strip()]
    query = Q()
    for country in selected_country:
        for product in selected_product:
            query |= Q(reporting_country__name=country, product_sector__name=product)

    # 查询数据库
    queryset = TradeYearData_I.objects.filter(query)
    print(queryset)
    # 将 TradeYearData_E 对象转为字典
    data = [{'year': entry.year, 'country': entry.reporting_country.name, 'product': entry.product_sector.name,
             'import_value_y': entry.import_value_y} for entry in queryset]
    return JsonResponse({'data': data})

def echarts_flow_data_export(request):
    # 在这里处理前端传递的参数，查询数据库，获取相应的数据
    # 将传递的字符串参数拆分成列表
    selected_time = [time.strip() for time in request.GET.get('time', '').split(',') if time.strip()]


    # 使用 Q 对象构建动态的查询条件
    query = Q()
    for time in selected_time:
        query |= Q(year=time, export_value__gt=200)
    
    # 查询数据库

    queryset = CommercialData_E_Individual.objects.filter(query)
    print(queryset)

    # 构建节点和边的列表
    nodes = set()
    edges = []

    for entry in queryset:
        reporting_country = entry.reporting_country.name
        partner_country = entry.partner_country.name
        export_value = entry.export_value

        # 添加国家节点及经纬度信息（如果经纬度不为空）
        reporting_country_node = {
            'name': reporting_country,
            'latitude': entry.reporting_country.latitude,
            'longitude': entry.reporting_country.longitude,
        }
        if entry.reporting_country.latitude is not None and entry.reporting_country.longitude is not None:
            nodes.add((reporting_country, entry.reporting_country.latitude, entry.reporting_country.longitude))

        partner_country_node = {
            'name': partner_country,
            'latitude': entry.partner_country.latitude,
            'longitude': entry.partner_country.longitude,
        }
        if entry.partner_country.latitude is not None and entry.partner_country.longitude is not None:
            nodes.add((partner_country, entry.partner_country.latitude, entry.partner_country.longitude))

        # 添加边（如果两个节点均存在）
        if (reporting_country, entry.reporting_country.latitude, entry.reporting_country.longitude) in nodes and (partner_country, entry.partner_country.latitude, entry.partner_country.longitude) in nodes:
            edges.append({
                'source': reporting_country,
                'target': partner_country,
                'value': export_value,
            })

    # 将节点和边的列表传递给前端
    data = {
        'nodes': list(nodes),
        'edges': edges,
    }

    return JsonResponse(data, safe=False)

def echarts_flow_data_import(request):
    # 在这里处理前端传递的参数，查询数据库，获取相应的数据
    # 将传递的字符串参数拆分成列表
    selected_time = [time.strip() for time in request.GET.get('time', '').split(',') if time.strip()]


    # 使用 Q 对象构建动态的查询条件
    query = Q()
    for time in selected_time:
        query |= Q(year=time, import_value__gt=200)
    
    # 查询数据库

    queryset = CommercialData_I_Individual.objects.filter(query)
    print(queryset)

    # 构建节点和边的列表
    nodes = set()
    edges = []

    for entry in queryset:
        reporting_country = entry.reporting_country.name
        partner_country = entry.partner_country.name
        import_value = entry.import_value

        # 添加国家节点及经纬度信息（如果经纬度不为空）
        reporting_country_node = {
            'name': reporting_country,
            'latitude': entry.reporting_country.latitude,
            'longitude': entry.reporting_country.longitude,
        }
        if entry.reporting_country.latitude is not None and entry.reporting_country.longitude is not None:
            nodes.add((reporting_country, entry.reporting_country.latitude, entry.reporting_country.longitude))

        partner_country_node = {
            'name': partner_country,
            'latitude': entry.partner_country.latitude,
            'longitude': entry.partner_country.longitude,
        }
        if entry.partner_country.latitude is not None and entry.partner_country.longitude is not None:
            nodes.add((partner_country, entry.partner_country.latitude, entry.partner_country.longitude))

        # 添加边（如果两个节点均存在）
        if (reporting_country, entry.reporting_country.latitude, entry.reporting_country.longitude) in nodes and (partner_country, entry.partner_country.latitude, entry.partner_country.longitude) in nodes:
            edges.append({
                'source': reporting_country,
                'target': partner_country,
                'value': import_value,
            })

    # 将节点和边的列表传递给前端
    data = {
        'nodes': list(nodes),
        'edges': edges,
    }

    return JsonResponse(data, safe=False)

def year_data_import(request):
    selectedcountry=request.GET['country']
    query = Q(reporting_country__name__contains=selectedcountry)
    queryset = TradeYearIndex_I.objects.filter(query)
    data=[]
    for entry in queryset:
        import_value = entry.import_value_i
        year=entry.year
        data.append({
            'year':year,
            'value':import_value,
        })
    return JsonResponse({'data': data}, safe=False)

def year_data_export(request):
    selectedcountry = request.GET['country']

    query = Q(reporting_country__name__contains=selectedcountry)
    queryset = TradeYearIndex_E.objects.filter(query)
    data = []
    for entry in queryset:
        export_value = entry.export_value_i
        year = entry.year
        data.append({
            'year': year,
            'value': export_value,
        })
    return JsonResponse({'data': data}, safe=False)
def quarter_data_import(request):
    selectedcountry = request.GET['country']
    query = Q(reporting_country__name__contains=selectedcountry)
    queryset = TradeQuarterData_I.objects.filter(query)
    data = []
    for entry in queryset:
        import_value = entry.import_value_q
        year = entry.year
        quarter=entry.quarter
        data.append({
            'year': year,
            'value': import_value,
            'quarter':quarter,
        })
    return JsonResponse({'data': data}, safe=False)
def quarter_data_export(request):
    selectedcountry = request.GET['country']
    query = Q(reporting_country__name__contains=selectedcountry)
    queryset = TradeQuarterData_E.objects.filter(query)
    data = []
    for entry in queryset:
        export_value = entry.export_value_q
        year = entry.year
        quarter=entry.quarter
        data.append({
            'year': year,
            'value': export_value,
            'quarter':quarter,
        })
    return JsonResponse({'data': data}, safe=False)
def month_data_import(request):
    selectedcountry = request.GET['country']
    query = Q(reporting_country__name__contains=selectedcountry)
    queryset = TradeMonthData_I.objects.filter(query)
    data = []
    for entry in queryset:
        import_value = entry.import_value_m
        year = entry.year
        month=entry.month
        data.append({
            'year': year,
            'value': import_value,
            'month':month,
        })
    return JsonResponse({'data': data}, safe=False)
def month_data_export(request):
    selectedcountry = request.GET['country']
    query = Q(reporting_country__name__contains=selectedcountry)
    queryset = TradeMonthData_E.objects.filter(query)
    data = []
    for entry in queryset:
        export_value = entry.export_value_m
        year = entry.year
        month=entry.month
        data.append({
            'year': year,
            'value': export_value,
            'month':month,
        })
    return JsonResponse({'data': data}, safe=False)
def annual_product_import(request):
    selectedproduct=request.GET['product']
    selectedtime = request.GET['time']
    query=Q(product_sector__name=selectedproduct,year=selectedtime)
    queryset=TradeYearData_I_Individual.objects.filter(query)
    data=[]
    for entry in queryset:
        value=entry.import_value_y
        country=entry.reporting_country.name
        data.append({
            'value':value,
            'name':country,
        })
    return JsonResponse({'data':data},safe=False)
def annual_product_export(request):
    selectedproduct=request.GET['product']
    selectedtime = request.GET['time']
    query=Q(product_sector__name=selectedproduct,year=selectedtime)
    queryset=TradeYearData_E_Individual.objects.filter(query)
    data=[]
    for entry in queryset:
        value=entry.export_value_y
        country=entry.reporting_country.name
        data.append({
            'value':value,
            'name':country,
        })
    return JsonResponse({'data':data},safe=False)
def year_heat_import(request):
    selectedtime=request.GET['year']
    query=Q(year=selectedtime)
    queryset=TradeYearIndex_I.objects.filter(query)
    data=[]
    for entry in queryset:
        value=entry.import_value_i
        country=entry.reporting_country.name
        data.append({
            'value':value,
            'name':country
        })
    return JsonResponse({'data':data},safe=False)

def year_heat_export(request):
    selectedtime=request.GET['year']
    query=Q(year=selectedtime)
    queryset=TradeYearIndex_E.objects.filter(query)
    data=[]
    for entry in queryset:
        value=entry.export_value_i
        country=entry.reporting_country.name
        data.append({
            'value':value,
            'name':country
        })
    return JsonResponse({'data':data},safe=False)
    
def country(request):
    # country_name = Country_L.objects.values_list('name', flat=True)
    # lat = Country_L.objects.values_list('latitude', flat=True)
    # lon = Country_L.objects.values_list('longitude', flat=True)
    query = Q()
    queryset = Country_L.objects.filter(query)
    data = []
    for entry in queryset:
        country_name = entry.name
        lat = entry.latitude
        lon = entry.longitude
        data.append({
            'Name': country_name,
            'Latitude': lat,
            'Longitude': lon,
        })
    return JsonResponse({'data': data}, safe=False)

def mfn_a(request):
    selectedyear=request.GET['year']
    query = Q(year=selectedyear)
    queryset = MFN_a.objects.filter(query)
    data = []
    for entry in queryset:
        country = entry.reporting_country.name
        year = entry.year
        value = entry.MFN_value
        data.append({
            'Reporting country': country,
            'Year': year,
            'MFN value': value,
        })
    return JsonResponse({'data': data}, safe=False)

def mfn_b(request):
    selectedyear=request.GET['year']
    query = Q(year=selectedyear)
    queryset = MFN_b.objects.filter(query)
    data = []
    for entry in queryset:
        country = entry.reporting_country.name
        product = entry.product_sector.name
        year = entry.year
        value = entry.MFN_value
        data.append({
            'Reporting country': country,
            'Product sector': product,
            'Year': year,
            'MFN value': value,
        })
    return JsonResponse({'data': data}, safe=False)

def test(request):
    return render(request, 'test.html')
def index(request):
    return render(request, 'index.html')
def blank(request):
    return render(request, 'pages/blank.html')
def home(request):
    return render(request, 'pages/home.html')
def login(request):
    return render(request, 'pages/login.html')
def p1(request):
    return render(request, 'pages/p1.html')
def p2(request):
    return render(request, 'pages/p2.html')
def p3(request):
    return render(request, 'pages/p3.html')
def p4(request):
    return render(request, 'pages/p4.html')
def p5(request):
    return render(request, 'pages/p5.html')
def p6(request):
    return render(request, 'pages/p6.html')
def p7(request):
    return render(request, 'pages/p7.html')
def p8(request):
    return render(request, 'pages/p8.html')
def p9(request):
    return render(request, 'pages/p9.html')
def p10(request):
    return render(request, 'pages/p10.html')

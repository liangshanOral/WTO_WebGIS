"""
URL configuration for webgis project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from wto.views import get_country_product_data, get_flow_data ,echarts_data, echarts_flow_data_export, echarts_flow_data_import, year_data_import, year_data_export,quarter_data_import,quarter_data_export,month_data_export,month_data_import,annual_product_import,annual_product_export,echarts_data_import,year_heat_import,year_heat_export, country, mfn_a, mfn_b


urlpatterns = [
    #path("select2/", include("django_select2.urls")),
    path('admin/', admin.site.urls),
    path('', include('wto.urls')),
    path('get-country-product-data/', get_country_product_data, name='get_country_product_data'),
    path('get-flow-data/',get_flow_data,name='get_flow_data'),
    path('echarts-data/', echarts_data, name='echarts_data'),
    path('echarts-data-import/', echarts_data_import, name='echarts_data_import'),
    path('echarts-flow-data-export/',echarts_flow_data_export,name="echarts_flow_data_export"),
    path('echarts-flow-data-import/',echarts_flow_data_import,name="echarts_flow_data_import"),
    path('year-data-import/',year_data_import,name="year_data_import"),
    path('year-data-export/',year_data_export,name="year_data_export"),
    path('quarter-data-import/',quarter_data_import,name="quarter_data_import"),
    path('quarter-data-export/',quarter_data_export,name="quarter_data_export"),
    path('month-data-import/',month_data_import,name="month_data_import"),
    path('month-data-export/',month_data_export,name="month_data_export"),
    path('annual-product-import/',annual_product_import,name="annual_product_import"),
    path('annual-product-export/',annual_product_export,name="annual_product_export"),
    path('year-heat-import/',year_heat_import,name="year_heat_import"),
    path('year-heat-export/',year_heat_export,name="year_heat_export"),
    path('country/', country, name="country"),
    path('mfn_a/', mfn_a, name="mfn_a"),
    path('mfn_b/', mfn_b, name="mfn_b"),
]

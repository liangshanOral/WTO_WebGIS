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
from wto.views import get_country_product_data, echarts_data, index

urlpatterns = [
    #path("select2/", include("django_select2.urls")),
    path('admin/', admin.site.urls),
    path('get-country-product-data/', get_country_product_data, name='get_country_product_data'),
    path('get')
    path('echarts-data/', echarts_data, name='echarts_data'),
    path('', index, name='index'),
]

from django.urls import path
from wto.views import test, index, blank, home, login, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10

urlpatterns = [
    path('', home, name='home'),

    #path('', test, name='test'),
    path('index/', index, name='index'),
    path('blank/', blank, name='blank'),
    path('home/', home, name='home'),
    path('login/', login, name='login'),
    path('control~p1', p1, name='p1'),
    path('control~p2', p2, name='p2'),
    path('control~p3', p3, name='p3'),
    path('control~p4', p4, name='p4'),
    path('control~p5', p5, name='p5'),
    path('control~p6', p6, name='p6'),
    path('control~p7', p7, name='p7'),
    path('example~p1', p8, name='p8'),
    path('example~p2', p9, name='p9'),
    path('example~p3', p10, name='p10'),
]

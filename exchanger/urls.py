from django.urls import path
from .views import *

urlpatterns = [
    path('', show_main, name='home'),
    path('fluctuations/', show_chart, name='fluctuations'),
    path('addrate/', add_rate, name='new_rate'),
]

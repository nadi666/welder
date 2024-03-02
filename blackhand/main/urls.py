from django.urls import path
from . import views

app_name = 'hand'

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.product_list, name='menu'),
]
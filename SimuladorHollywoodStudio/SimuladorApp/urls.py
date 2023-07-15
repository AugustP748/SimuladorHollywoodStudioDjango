from django.contrib import admin
from django.urls import path
from . import views

app_name="Simulador"
urlpatterns = [
    path('', views.home, name='home'),
    path('table-data/', views.get_table_data,name='get_table_data'),
]

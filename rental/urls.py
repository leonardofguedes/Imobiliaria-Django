from django.urls import path
from . import views


#app_name = 'rental'

urlpatterns = [
    path('', views.ListViewBase.as_view(), name="imobiliaria-home"),
    path('imovel/search/', views.ListViewSearch.as_view(), name='search'),
    path('imovel/<int:category_id>/', views.imovel, name='imoveis-house'),
]


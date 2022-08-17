from django.urls import path
from . import views


#app_name = 'rental'

urlpatterns = [
    path('', views.HomeListView.as_view(), name="imobiliaria-home"),
    path('imovel/search/', views.ListViewSearch.as_view(), name='search'),
    path('imovel/<int:pk>/', views.Detail.as_view(), name='imoveis-house'),
]

from django.urls import path
from .views import home, imovel, search


#app_name = 'rental'

urlpatterns = [
    path('imovel/search/', search, name='search'),
    path('', home, name='imobiliaria-home'),
    path('imovel/<int:category_id>/', imovel, name='imoveis-house'),
]


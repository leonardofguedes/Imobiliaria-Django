from django.urls import path
from .views import home, imovel

urlpatterns = [
    path('', home, name='imobiliaria-home'),
    path('imovel/<int:category_id>/', imovel, name='imoveis-house') #ler path converters
]
from django.urls import path
from . import views

app_name = 'authors'

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('create/', views.register_create, name='create')
]




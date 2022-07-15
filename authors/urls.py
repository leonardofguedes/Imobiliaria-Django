from django.urls import path
from . import views

app_name = 'authors'

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('register/create/', views.register_create, name='register_create'),
    path('login/', views.login_view, name='login'),
    path('login/create', views.login_create, name='login_create'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path(
        'dashboard/imovel/delete/',
        views.Dashboard_Delete.as_view(),
        name='dashboard_imovel_delete'
    ),
    path(
        'dashboard/imovel/new/',
        views.Dashboard_Imovel.as_view(),
        name='dashboard_imovel_new'
    ),
    path(
        'dashboard/imovel/<int:id>/edit/',
        views.Dashboard_Imovel.as_view(),
        name='dashboard_imovel_edit'
    ),
]




from . import views
from django.urls import path

app_name = 'template_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('base/', views.base, name='base'),
    path('main/', views.main, name='main'),
]

from . import views
from django.urls import path

app_name = 'template_app'
urlpatterns = [
    path('base/', views.base, name='base'),
    path('main/', views.main, name='main'),
]

from . import views
from django.urls import path

app_name = 'template_app'
urlpatterns = [
    path('base/', views.index, name='index'),
    path('main/', views.main, name='main'),
]

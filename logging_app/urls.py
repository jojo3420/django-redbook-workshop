from django.urls import path
from . import views

app_name = 'logging_app'
urlpatterns = [
    path('', views.index, name='index'),
]
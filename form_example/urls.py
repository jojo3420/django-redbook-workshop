from django.urls import path
from . import views

app_name = 'form_example'
urlpatterns = [
    path('', views.index, name='index'),
    path('your-name/', views.your_name, name='your_name'),
    path('thanks/', views.thanks, name='thanks'),
    path('contact/', views.contact_form, name='contact_form'),

]


from django.db import models
from django.utils import timezone
from django import forms


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=30)
    publisher = models.CharField(max_length=50)
    publication_date = models.DateTimeField(default=timezone.now)


class MyForm(forms.Form):
    title = forms.CharField(label='title', max_length=200)
    subject = forms.CharField(max_length=500, widget=forms.Textarea)
    date = forms.DateTimeField()
    email = forms.EmailField()
    y_n = forms.BooleanField(required=False)

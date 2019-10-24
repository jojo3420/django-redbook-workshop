from django.db import models
from django.utils import timezone


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=30)
    publisher = models.CharField(max_length=50)
    publication_date = models.DateTimeField(default=timezone.now)

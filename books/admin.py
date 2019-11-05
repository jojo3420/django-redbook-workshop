from django.contrib import admin
from books.models import Book
from books.models import Author
from books.models import Publisher
# 하나의 코드는 한가지 일만 한다. 규칙


admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Publisher)






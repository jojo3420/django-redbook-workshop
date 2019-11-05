from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    # N:N 관계 :  1권의 책은 여려명의 저자를 가질 수 있고 하나의 저자도 여려권의 책의 저자가 될 수 있다.
    authors = models.ManyToManyField('Author')
    # N:1 관계 : 여러권의 책과 하나의 출판사와 관계로 한권의 책은 하나의 출판사에만 관련되지만 출판사는 여러권의 책과 관련되어 있다.
    # ForeignKey 필드는 반드시 on_delete 옵션이 필수
    # publisher 테이블의 특정 레코드가 삭제되면 그 레코드와 연결된 Book 테이블의 레코드도 삭제 된다.
    publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE)

    publication_date = models.DateField()

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=50)
    salutation = models.CharField(max_length=100, verbose_name='저자 인사말')
    email = models.EmailField()

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    website = models.URLField()

    def __str__(self):
        return self.name

from django.db import models
from KALib import settings
from django.contrib.auth.models import User


# Create your models here.

class Book(models.Model):
    name = models.TextField()
    img = models.ImageField(upload_to=settings.MEDIA_ROOT + '/img')
    path = models.FileField(upload_to=settings.MEDIA_ROOT + '/books')
    rating = models.FloatField()
    rates = models.IntegerField()
    created_data = models.DateTimeField()
    amount_views = models.IntegerField()

    def __str__(self):
        return self.name


class Attrib(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    name = models.TextField()
    value = models.TextField()

    def __str__(self):
        return "name = {0} value ={1}".format(self.name, self.value)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return "first_name = {0} text = {1}".format(self.user.first_name, self.text)


class Rate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rate = models.IntegerField()

    def __str__(self):
        return "first_name = {0} book ={1} rate ={1}".format(self.user.first_name, self.book.name, self.rate)


class Category(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name


class CategoryAndBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Author(models.Model):
    name = models.TextField()
    surname = models.TextField()
    birthday = models.DateField()
    info = models.TextField()


class AuthorAndBook(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)


class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

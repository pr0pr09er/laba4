from django.db import models


# Create your models here.
class Category(models.Model):
    genre = models.CharField(max_length=50)


class Film(models.Model):
    name = models.CharField(max_length=100)
    genre = models.ForeignKey(Category, on_delete=models.CASCADE)
    issue_date = models.DateField()
    actors = models.TextField()
    show_date = models.DateField()

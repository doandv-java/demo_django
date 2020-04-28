from django.db import models


# Create your models here.
class Store(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField(max_length=200)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=20)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    store_names = []

    def __str__(self):
        return self.name

    def name_store(self):
        return self.store.name

    def store_names(self):
        for name in self.store:
            self.store_names.append(name)


class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    cost = models.FloatField(default=0.0)
    page_number = models.IntegerField(default=0)

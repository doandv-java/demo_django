from django.db import models


# Create your models here.
class Store(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField(max_length=200)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=50)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def categories_of_store(self):
        return Category.objects.filter(store_id=self.id)

    def books_of_store(self):
        categories = Category.objects.filter(store_id=self.id)
        return Book.objects.filter(category__in=categories)


class Category(models.Model):
    name = models.CharField(max_length=20)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def name_store(self):
        return self.store.name

    def books_of_category(self):
        return Book.objects.filter(category_id=self.id)


class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    cost = models.FloatField(default=0.0)
    page_number = models.IntegerField(default=0)

    def __str__(self):
        return self.name

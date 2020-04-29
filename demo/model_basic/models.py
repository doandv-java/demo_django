from django.db import models


# Create your models here.
class Person(models.Model):
    GENDERS = ((0, 'MALE'), (1, 'FEMALE'))
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        return self.first_name + self.last_name


class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        return self.first_name + self.last_name


class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.PositiveSmallIntegerField(default=0)


'''
    For example, if a Car model has a Manufacturer – 
    that is, a Manufacturer makes multiple cars but each Car
    only has one Manufacturer – use the following definitions:
'''


# One to Many
class Manufacturer(models.Model):
    name = models.CharField(max_length=20)


class Car(models.Model):
    name = models.CharField(max_length=50)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)


# Many to many field
class Topping(models.Model):
    name = models.CharField(max_length=50)


class Pizza(models.Model):
    name = models.CharField(max_length=50)
    toppings = models.ManyToManyField(Topping)


# Many to many
class Group(models.Model):
    name = models.CharField(max_length=18)
    members = models.ManyToManyField(Person, through='Membership')


class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invited_reason = models.CharField(max_length=64)


# Abstract
class Animal(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        abstract = True
        ordering = ['name']


class Cat(Animal):
    class Meta(Animal.Meta):
        db_table = 'db_cat'

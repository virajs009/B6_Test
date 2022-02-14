from django.db import models

# Create your models here.

class InactiveBooksManager(models.Manager):                     # defining custom model manager
    def get_queryset(self):
        return super(InactiveBooksManager, self).get_queryset().filter(is_active="N")

class Book(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    qty = models.IntegerField()
    is_active = models.CharField(max_length=1, default="Y")
    objects = models.Manager()                                  # Default model manager
    inactive_books = InactiveBooksManager()                     # custom model manager

    class Meta:
        db_table = 'book'

    def __str__(self):
        return f"{self.name}"

class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    mobile = models.CharField(max_length=10)
    email = models.EmailField()

    class Meta:
        db_table = "emp"

    def __str__(self):
        return self.first_name


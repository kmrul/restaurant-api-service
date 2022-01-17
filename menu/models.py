from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(default=0, decimal_places=2, max_digits=10)
    createAt = models.DateTimeField(auto_now_add=True)
    updateAt = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

class MenuItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    publish_date = models.DateField(auto_now_add=True)
    createAt = models.DateTimeField(auto_now_add=True)
    updateAt = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)


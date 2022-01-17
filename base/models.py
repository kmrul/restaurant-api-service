from dataclasses import field
from statistics import mode
from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updateAt = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
from django.db import models
from django.utils import timezone

"""
CONTACTS
name: STR * (mandatory)
surname: STR * (mandatory)
telephone: STR * (mandatory)
email: STR (optional)
date: DATETIME (automatic)
description: text
category: CATEGORY (other model)

CATEGORY:
name: STR * (mandatory)
"""

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255, blank=True)
    telephone = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True)
    date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to='pictures/%Y%m')

    def __str__(self):
        return self.name
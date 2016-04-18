from __future__ import unicode_literals

from django.db import models

from aec.apps.library.models import Library

from .managers import CustomManager

class Dictionary(models.Model):
    word = models.CharField(max_length=50, unique=True)
    translate = models.CharField(max_length=100)
    synonym = models.ManyToManyField("self", blank=True)
    antonym = models.ManyToManyField("self", blank=True)
    library = models.ManyToManyField(Library, blank=True)

    objects = CustomManager()

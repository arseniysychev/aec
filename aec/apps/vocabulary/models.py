from __future__ import unicode_literals

from django.db import models

# from aec.validators import is_english
from aec.apps.library.models import Library
from .managers import CustomManager


class Word(models.Model):
    english = models.CharField(max_length=50, unique=True)
    translate = models.CharField(max_length=100)
    antonym = models.ManyToManyField("self", blank=True)
    library = models.ManyToManyField(Library, blank=True)

    objects = CustomManager()

    def __str__(self):
        return '{en} - {translate}'.format(
            en=self.english,
            translate=self.translate
        )

from __future__ import unicode_literals

from django.db import models

LEVELS_CHOICES = (
    (0, 'BLES level'),
    (1, 'GRAS level'),
    (2, 'GRAS level'),
    (3, 'GRAS level'),
    (4, 'GRAS level'),
    (5, 'GRAS level'),
    (6, 'GRAS level'),
    (7, 'HIGH level'),
)


class Library(models.Model):
    level = models.PositiveSmallIntegerField(choices=LEVELS_CHOICES,
                                             blank=True, null=True)
    lesson = models.PositiveSmallIntegerField(blank=True, null=True)

    class Meta:
        unique_together = ("level", "lesson")

    def __str__(self):
        return '{level}({name}) lesson - {lesson}'.format(
            level=self.level,
            name=self.get_level_display(),
            lesson=self.lesson
        )

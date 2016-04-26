from django.contrib import admin

from aec.apps.library.models import Library
from aec.apps.vocabulary.models import Word

admin.site.register(Library)
admin.site.register(Word)

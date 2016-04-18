from django.conf.urls import url, include
from django.contrib import admin

from .views import index

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^vocabulary/', include('aec.apps.vocabulary.urls')),
    url(r'^$', index),
]

from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

from aec.apps.library.views import LibraryViewSet
from aec.apps.vocabulary.views import VocabularyViewSet
from .views import index

router = DefaultRouter()
router.register(r'vocabulary', VocabularyViewSet)
router.register(r'library', LibraryViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^$', index),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

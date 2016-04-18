from rest_framework.routers import DefaultRouter
from django.conf.urls import url, include

from .views import DictionaryViewSet

router = DefaultRouter()
router.register(r'dict', DictionaryViewSet)

# urlpatterns = [
#     url(r'^', include(router.urls)),
# ]
urlpatterns = router.urls

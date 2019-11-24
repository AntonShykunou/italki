from django.conf.urls import include
from django.urls import path
from .views import LanguageViewSet
from rest_framework.routers import DefaultRouter

app_name = 'languages'

router = DefaultRouter()
router.register(r'languages', LanguageViewSet, basename='language')
urlpatterns = router.urls

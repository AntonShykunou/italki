from django.conf.urls import include
from django.urls import path
from .views import LanguageViewSet, LearningLanguageViewSet
from rest_framework.routers import DefaultRouter

app_name = 'languages'

router = DefaultRouter()
router.register(r'languages', LanguageViewSet, basename='language')
router.register(r'learninglanguage', LearningLanguageViewSet, basename='learninglanguage')
urlpatterns = router.urls

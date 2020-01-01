from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UploadPhotoView, UserViewSet
from lessons.views import LessonListView

router = DefaultRouter()
router.register(r'', UserViewSet)

urlpatterns = [
    path('users/', include(router.urls)),
    path('users/<int:id>/lessons', LessonListView.as_view()),
    path('users/<int:pk>/upload_photo', UploadPhotoView.as_view()),
]

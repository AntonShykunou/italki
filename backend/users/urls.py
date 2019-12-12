from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users import views
from lessons.views import LessonListView


app_name = "users"

router = DefaultRouter()
router.register(r'', views.UserViewSet)

urlpatterns = [
    path('users/', include(router.urls)),
    path('users/<int:id>/lessons', LessonListView.as_view())
]


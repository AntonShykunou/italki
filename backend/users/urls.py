from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users import views


router = DefaultRouter()
router.register(r'', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import FeedbackCreateView, FeedbackDeleteView
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'feedbacks', FeedbackCreateView)
router.register(r'feedbacks', FeedbackDeleteView)


app_name = "feedbacks"

urlpatterns = [
    path(r'feedbacks', FeedbackCreateView.as_view()),
    path(r'feedbacks/<int:id>', FeedbackDeleteView.as_view())
]


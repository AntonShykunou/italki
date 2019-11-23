from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import FeedbackListView, FeedbackDetailView


app_name = "feedbacks"

urlpatterns = [
    path(r'feedbacks', FeedbackListView.as_view()),
    path(r'feedbacks/<int:id>', FeedbackDetailView.as_view())
]


from django.urls import path
from lessons.views import LessonListView


app_name = "users"

urlpatterns = [
    path('users/<int:id>/lessons', LessonListView.as_view()),
]
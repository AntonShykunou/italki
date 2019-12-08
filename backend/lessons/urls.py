from django.urls import path
from .views import LessonListView, LessonSessionListView, LessonRetrieveUpdateDestroyView


app_name = "lessons"

urlpatterns = [
    path('users/<int:id>/lessons', LessonListView.as_view()),
    path('lessons/<int:pk>', LessonRetrieveUpdateDestroyView.as_view()),
    path('lessonsessions/', LessonSessionListView.as_view())
]

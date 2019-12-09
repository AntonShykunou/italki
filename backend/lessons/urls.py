from django.urls import path
from .views import LessonSessionListView, LessonRetrieveUpdateDestroyView


app_name = "lessons"

urlpatterns = [
    path('lessons/<int:pk>', LessonRetrieveUpdateDestroyView.as_view()),
    path('lessonsessions/', LessonSessionListView.as_view())
]

from django.urls import path
from .views import LessonRetrieveUpdateDestroyView, LessonSessionView, LessonSessionApprovedView, LessonSessionDetailView, LessonSessionDeclinedView, LessonSessionFinishedView


app_name = "lessons"

urlpatterns = [
    path('lessons/<int:pk>', LessonRetrieveUpdateDestroyView.as_view()),
    path('lessonsessions/', LessonSessionView.as_view()),
    path('lessonsessions/<int:pk>', LessonSessionDetailView.as_view()),
    path('lessonsessions/<int:pk>/approval', LessonSessionApprovedView.as_view()),
    path('lessonsessions/<int:pk>/decline',LessonSessionDeclinedView.as_view()),
    path('lessonsessions/<int:pk>/finish', LessonSessionFinishedView.as_view())
]

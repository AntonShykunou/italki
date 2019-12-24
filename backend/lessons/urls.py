from django.urls import path
from .views import (LessonRetrieveUpdateDestroyView, LessonSessionView, 
                LessonSessionApproveView, LessonSessionDetailView, 
                LessonSessionDeclineView, LessonSessionFinishView
            )


app_name = "lessons"

urlpatterns = [
    path('lessons/<int:pk>', LessonRetrieveUpdateDestroyView.as_view()),
    path('lessonsessions/', LessonSessionView.as_view()),
    path('lessonsessions/<int:pk>', LessonSessionDetailView.as_view()),
    path('lessonsessions/<int:pk>/approve', LessonSessionApproveView.as_view()),
    path('lessonsessions/<int:pk>/decline',LessonSessionDeclineView.as_view()),
    path('lessonsessions/<int:pk>/finish', LessonSessionFinishView.as_view())
]

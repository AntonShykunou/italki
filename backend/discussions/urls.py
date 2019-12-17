from django.conf.urls import include
from django.urls import path
from .views import DiscussionListView, DiscussionDetailView, DiscussionCreateView, DiscussionCommentsCreateView

app_name = "discussions"

urlpatterns = [
    path('discussions/', DiscussionListView.as_view()),
    path('discussions/<int:pk>', DiscussionDetailView.as_view()),
    path('discussions/<int:pk>/comment', DiscussionCommentsCreateView.as_view()),
    path('discussions/new', DiscussionCreateView.as_view()),
    path('discussions/(?P<user_id>.+)/$', DiscussionListView.as_view()),
]

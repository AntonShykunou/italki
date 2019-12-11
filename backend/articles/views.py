from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Article
from .serializers import ArticleSerializer
from likes.mixins import LikedMixin



class ArticleViewSet(LikedMixin,viewsets.ModelViewSet):
    queryset = Article.objects.for_user()
    serializer_class = ArticleSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
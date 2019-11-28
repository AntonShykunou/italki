from .models import Teacher
from .serializers import TeacherSerializer
from rest_framework import viewsets,generics, mixins, views
from django_filters import rest_framework as filters
from .pagination import StandardResultsSetPagination

class TeacherViewSet(
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     mixins.ListModelMixin,
                     viewsets.GenericViewSet):

    queryset = Teacher.objects.all()\
        .prefetch_related('user')\
        .prefetch_related('user__native_languages')
    serializer_class = TeacherSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('user__native_languages__title',)
    
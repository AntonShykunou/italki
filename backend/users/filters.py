import django_filters
from .models import Teacher

def filter_teachers(queryset, name, value):
    return queryset.filter(user__native_languages__title=value)

class TeacherFilterSet(django_filters.FilterSet):
    native_language = django_filters.CharFilter(field_name='', method=filter_teachers)

    class Meta:
        model = Teacher
        fields = ['native_language']
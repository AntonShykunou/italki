from .models import LessonSession
from .choices import CHOICES_STATUS
import django_filters
from users.models import User, Teacher

def filter_teachers(queryset, name, value):
    return queryset.filter(lesson__teacher=value)

class LessonSessionFilterSet(django_filters.FilterSet):
    status = django_filters.ChoiceFilter(choices=CHOICES_STATUS)
    teacher_id = django_filters.CharFilter(field_name='', method=filter_teachers)

    class Meta:
        model = LessonSession
        fields = ['teacher_id', 'status']
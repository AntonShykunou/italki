from .models import LessonSession
from .choises import CHOISES_STATUSE
import django_filters
from users.models import User, Teacher


class LessonSessionFilterSet(django_filters.FilterSet):
    status = django_filters.ChoiceFilter(choices=CHOISES_STATUSE)
    # teacher_id = django_filters.ModelChoiceFilter(name='lesson_teacher_id', queryset=Teacher.objects.all())
    class Meta:
        model = LessonSession
        fields = ['status']
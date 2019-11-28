from .views import TeacherViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'teachers', TeacherViewSet)

app_name = "teachers"

urlpatterns = router.urls

from django.config.urls import url

from .views import ReferralView


urlpatterns = [
	url(r"^(?P<identifier>\w+)$", ReferralView.as_view()),
]
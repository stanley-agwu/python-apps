from django.conf.urls import url
from .views import CarAPIView

urlpatterns = [
    url('cars/', CarAPIView.as_view()),
]
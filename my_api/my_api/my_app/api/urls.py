from django.conf.urls import url, include
from .views import hello_world

urlpatterns = [
    url('first/', hello_world),
]
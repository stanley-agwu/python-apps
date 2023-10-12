from django.conf.urls import url, include
from .views import CourseViewSet, StudentViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('courses', CourseViewSet, basename='courses')
router.register('students', StudentViewSet, basename='students')
# urlpatterns = router.urls

urlpatterns = [
    url('', include(router.urls)),
]
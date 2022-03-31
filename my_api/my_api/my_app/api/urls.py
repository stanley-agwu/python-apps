from django.conf.urls import url, include
from .views import CarSpecificationViewset

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('car-specs', CarSpecificationViewset, basename='car-specs')
urlpatterns = router.urls

# urlpatterns = [
#     url('', include(router.urls)),
# ]
from django.conf.urls import url, include
from .views import PostViewSet, PostsRateViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
router.register('posts-rate', PostsRateViewSet, basename='posts-rate')
# urlpatterns = router.urls

urlpatterns = [
    url('', include(router.urls)),
]
from rest_framework import routers
from .api import PostViewSet
from django.conf.urls import url, include


router = routers.DefaultRouter()
router.register('post', PostViewSet, basename='post')

urlpatterns = [
    url(r'^api/', include(router.urls))
]

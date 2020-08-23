from django.urls import include, path
from rest_framework import routers

from .views import UserViewSet, UserCreate

router = routers.DefaultRouter()
router.register(r'', UserViewSet)
router.register(r'', UserCreate, basename='User')

urlpatterns = [
    path('', include(router.urls))
]

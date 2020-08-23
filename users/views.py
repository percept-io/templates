from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework.permissions import DjangoModelPermissions

from .models import CustomUser
from .serializers import UserFullSerializer, UserPasswordSerializer


# Create your views here.
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserFullSerializer
    permission_classes = [DjangoModelPermissions]


class UserCreate(viewsets.GenericViewSet, mixins.CreateModelMixin):
    serializer_class = UserPasswordSerializer
    permission_classes = [DjangoModelPermissions]

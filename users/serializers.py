from rest_framework import serializers

from .models import CustomUser


class UserFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'is_staff', 'is_active', 'date_joined']

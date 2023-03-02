from django.contrib.auth.models import User
from rest_framework import serializers

from .models import UserProfile, Room


class RoomSerial(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'name', 'owner']


class UserSerial(serializers.ModelSerializer):
    user_rooms = RoomSerial(many=True, read_only=True)
    class Meta:
        model = User
        fields = ['id','username', 'user_rooms']


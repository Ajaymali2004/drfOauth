from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Item

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class ItemSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Item
        fields = ('id', 'title', 'description', 'created_at', 'updated_at', 'user')
        read_only_fields = ('created_at', 'updated_at', 'user') 
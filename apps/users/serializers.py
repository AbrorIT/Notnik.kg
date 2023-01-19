from rest_framework import serializers
from apps.users.models import User 
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string
from threading import Thread

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = "__all__"

class UserCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = "__all__"

class UserUpdateSerializers(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = "__all__"






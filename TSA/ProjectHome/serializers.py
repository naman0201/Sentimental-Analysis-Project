import imp
from attr import fields
from rest_framework import serializers
from ProjectHome.models import webUser

class webuserSerializer(serializers.ModelSerializer):
    class Meta:
        model = webUser
        fields = '__all__'
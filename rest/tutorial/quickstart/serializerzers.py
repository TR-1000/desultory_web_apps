from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'group']

class GroupSeriaizer(serializer.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'name']        

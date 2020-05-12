from django.contrib.auth.models import User
from management import serializer
from management.serializer import UserSerializerList
from rest_framework import permissions
from rest_framework.generics import UpdateAPIView, GenericAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated


class UsersList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializerList

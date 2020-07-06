from django.shortcuts import render

# Create your views here.

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from backend.serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class LogViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows logs to be viewed or edited.
    """
    queryset = Log.objects.all()
    serializer_class = LogSerializer

class ListUsers(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)

    # https://www.instagram.com/jonathanperez16/
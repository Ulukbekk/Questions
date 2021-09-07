from django.shortcuts import render
from .permissions import IsOwner
from .serializers import AccountRegistrationSerializer
from rest_framework import generics, permissions


class AccountRegisterAPIView(generics.CreateAPIView):
    """
    This endpoint registers users based on the fields
    """
    serializer_class = AccountRegistrationSerializer
    permission_classes = (permissions.AllowAny,)


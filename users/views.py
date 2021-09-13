from django.shortcuts import render

from .models import Account
from .permissions import IsOwner
from .serializers import AccountRegistrationSerializer, AccountDetailSerializer
from rest_framework import generics, permissions


class AccountRegisterAPIView(generics.CreateAPIView):
    """
    This endpoint registers users based on the fields
    """
    serializer_class = AccountRegistrationSerializer
    permission_classes = (permissions.AllowAny,)

class AccountDetailAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = AccountDetailSerializer
    queryset = Account.objects.all()
    permission_classes = (permissions.IsAuthenticated, IsOwner)


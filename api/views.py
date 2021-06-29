from .models import User
from django.shortcuts import render

from .serializers import UserSerializer

from rest_framework.generics import ListAPIView

class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filterset_fields = ['city','first_name','last_name','age','email','mobile_no','education','create_at']
    



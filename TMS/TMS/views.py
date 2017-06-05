from rest_framework import viewsets
from serializer import UserModelSerializer
from .models import UserModel


class UserViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows users to be viewed or edited.
	"""
	queryset = UserModel.objects.all().order_by('-date_joined')
	serializer_class = UserModelSerializer

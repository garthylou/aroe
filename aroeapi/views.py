from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework.parsers import FormParser,MultiPartParser,FileUploadParser
from rest_framework import status
from aroeapi import models
from aroeapi import serializers
from django.core.files import File
import logging

logger = logging.getLogger(__name__)

class MembersViewSet(viewsets.ModelViewSet):
	queryset = models.Member.objects.all()
	serializer_class = serializers.MemberSerializer

class AvatarMemberViewSet(viewsets.ModelViewSet):
	queryset = models.Member.objects.all()
	serializer_class = serializers.AvatarMemberSerializer

class TrainingViewSet(viewsets.ModelViewSet):
	queryset = models.Training.objects.all()
	serializer_class = serializers.TrainingSerializer
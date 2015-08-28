from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework.parsers import FormParser,MultiPartParser,FileUploadParser
from rest_framework import status
from aroeapi import models
from aroeapi import serializers
from django.core.files import File
from rest_framework.decorators import api_view, permission_classes, throttle_classes
from rest_framework.permissions import AllowAny
from rest_framework.throttling import AnonRateThrottle
from rest_framework import status
from django.utils.translation import ugettext_lazy as _
from rest_framework.settings import api_settings
from rest_framework_csv import renderers as r
from core.image_processing import ImageProcessor
from django.conf import settings
from django.core.mail import send_mail

from PIL import Image, ExifTags
import os,sys

import logging

logger = logging.getLogger(__name__)

MAX_WIDTH = 800
MAX_HEIGHT= 600

class MembersViewSet(viewsets.ModelViewSet):
	queryset = models.Member.objects.all()
	serializer_class = serializers.MemberSerializer
	renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES + [r.CSVRenderer, ] 

class AvatarMemberViewSet(viewsets.ModelViewSet):
	queryset = models.Member.objects.all()
	serializer_class = serializers.AvatarMemberSerializer

	def perform_create(self, serializer):
		instance = serializer.save()
		# Perform post-processing treatment
		self.post_process(instance)

	def perform_update(self, serializer):
		old_photo = self.get_object().photo
		instance = serializer.save()
		if old_photo :
			os.remove(old_photo.path)
		self.post_process(instance)

	def post_process(self, instance ):
		if instance.photo :
			img_proc = ImageProcessor(instance.photo.path)
			try :
				img_proc.auto_orient()
				img_proc.resize(800,600)
			except NameError as e:
				logger.error(sys.exc_info()[0])
				logger.error(e)

class TrainingViewSet(viewsets.ModelViewSet):
	queryset = models.Training.objects.all()
	serializer_class = serializers.TrainingSerializer


@api_view(['POST'])
@permission_classes((AllowAny,))
@throttle_classes([AnonRateThrottle,])
def send_message(request):
	if request.data['from'] and request.data['to'] and request.data['message']:
		
		if request.data['to'] == 'association':
			logger.info("Try to send message to association %s, from %s : %s" % (
				request.data['to'],
				request.data['from'],
				request.data['message']
				)
			)
			send_mail('[Site AROE] - Contact', request.data['message'], request.data['from'],
    			[settings.EMAIL_ASSOCIATION], fail_silently=False)
		else :
			# Find the matching user
			member = models.Member.objects.get(pk=request.data['to'])
			logger.info("Try to send message to user %s, from %s : %s" % (
				member.family_name,
				request.data['from'],
				request.data['message']
				)
			)
			send_mail('[Site AROE] - Contact direct', request.data['message'], request.data['from'],
    		[member.email], fail_silently=False)
		#return Response(_("Your message has not been sent, because it does not work on this environment"), status=status.HTTP_400_BAD_REQUEST)
		return Response(_("Your message has been sent."))
	return Response("Not authorized.",status=status.HTTP_400_BAD_REQUEST)

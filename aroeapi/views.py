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
		# Get the image and obtain its orientation
		self.fix_orientation(instance)

	def perform_update(self, serializer):
		old_photo = self.get_object().photo
		instance = serializer.save()
		if old_photo :
			os.remove(old_photo.path)
		self.fix_orientation(instance)

	def fix_orientation(self, instance ):
		if instance.photo :
			try :
				image = Image.open(instance.photo.path)
				if hasattr(image, '_getexif'):
					for orientation in ExifTags.TAGS.keys():
						if ExifTags.TAGS[orientation]=='Orientation':
							break 
        			e = image._getexif()       # returns None if no EXIF data
        			if e is not None:
        				exif=dict(e.items())
        				orientation = exif[orientation]
        				if orientation == 3: 
        					image = image.transpose(Image.ROTATE_180)
        				elif orientation == 6: 
        					image = image.transpose(Image.ROTATE_270)
        				elif orientation == 8: 
        					image = image.transpose(Image.ROTATE_90)
        				else:
        					pass
        				image.save(instance.photo.path)

        			# Resize image to be compliant with WEB
        			s = image.size
        			ratio_width = s[0]/MAX_WIDTH
        			ratio_height = s[1]/MAX_HEIGHT
        			logger.info("ratio w = %s, ratio h = %s"% (ratio_width, ratio_height))
        			if (ratio_width > 1 or ratio_height > 1):
        				ratio = max(ratio_width, ratio_height)
        				image = image.resize((int(s[0]/ratio), int(s[1]/ratio)),Image.ANTIALIAS)
        				image.save(instance.photo.path)
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
		else :
			# Find the matching user
			member = models.Member.objects.get(pk=request.data['to'])
			logger.info("Try to send message to user %s, from %s : %s" % (
				member.family_name,
				request.data['from'],
				request.data['message']
				)
			)
		return Response(_("Your message has not been sent, because it does not work on this environment"), status=status.HTTP_400_BAD_REQUEST)
		#return Response(_("Your message has been sent."))
	return Response("Not authorized.",status=status.HTTP_400_BAD_REQUEST)

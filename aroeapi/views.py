from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework.parsers import FormParser,MultiPartParser,FileUploadParser
from rest_framework import status
from aroeapi import models
from aroeapi import serializers
from django.core.files import File
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import status
from django.utils.translation import ugettext_lazy as _
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


@api_view(['POST'])
@permission_classes((AllowAny,))
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

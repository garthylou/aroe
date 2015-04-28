from rest_framework import serializers
from aroeapi import models
from wagtail.wagtaildocs.models import Document

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Member

class AvatarMemberSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Member
		fields = ('id', 'photo')

class DocumentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Document
		exclude = ('uploaded_by_user',)
		read_only_fields = ('title','file','created_at',)


class TrainingSerializer(serializers.ModelSerializer):
	document_detail = DocumentSerializer(source='document',read_only=True)
	class Meta:
		model = models.Training
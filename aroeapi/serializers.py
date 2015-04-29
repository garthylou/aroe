from rest_framework import serializers
from aroeapi import models
from wagtail.wagtaildocs.models import Document
from wagtail.wagtailcore.models import Page

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

class PageSerializer(serializers.ModelSerializer):
	class Meta:
		model = Page
		fields = ('id','title', 'url',)


class TrainingSerializer(serializers.ModelSerializer):
	document_detail = DocumentSerializer(source='document',read_only=True)
	page_detail = PageSerializer(source='page',read_only=True)
	class Meta:
		model = models.Training
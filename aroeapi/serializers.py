from rest_framework import serializers
from aroeapi import models

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Member

class AvatarMemberSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Member
		fields = ('id', 'photo')
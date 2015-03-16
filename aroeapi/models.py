from django.db import models

from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError
from django.core.exceptions import NON_FIELD_ERRORS
from datetime import date, datetime



def path_members_photo(instance, filename):
	"""
	Function to define the url to access to image for members
	"""
	if instance.id is not None :
		return 'members/photo/%s-%s-%s' % (instance.id, instance.family_name,instance.firstname)
	else:
		return 'members/photo/%s-%s' % (instance.family_name,instance.firstname)

class Member(models.Model):
	family_name = models.CharField(_('Family name'), max_length=200)
	firstname = models.CharField(_('First name'), max_length=200)
	address = models.CharField(_('Address'), max_length=500, blank=True)
	zipcode = models.CharField(_('Zipcode'), max_length=10, blank=True)
	city = models.CharField(_('City'), max_length=200, blank=True)
	phone = models.CharField(_('Phone'), max_length=100, blank=True)
	email = models.EmailField(_('Email'), max_length=254,blank=True)
	photo = models.ImageField(_('Photo'),upload_to=path_members_photo, blank=True, null=True)

	def __unicode__(self):
		return "{0} {1} {2}".format( self.family_name, self.firstname, self.zipcode )


class Training(models.Model):
	title = models.CharField(_('Title'), max_length=200)
	start = models.DateField(_('Start'))
	end = models.DateField(_('End'),blank=True, null=True)
	description = models.TextField(_('Description'), blank=True, null=True)
	responsible = models.CharField(_('Responsible'), max_length=200, blank=True, null=True)
	intervenant = models.CharField(_('Intervenant'), max_length=250, blank=True, null=True)
	seats = models.PositiveIntegerField(_('Seats'),blank=True, null=True)
	occupied_seats = models.PositiveIntegerField(_('Seats'), blank=True, null=True)
	location = models.CharField(_('Location'), max_length=300, blank=True, null=True)

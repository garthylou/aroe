from django import template
import datetime

from aroeapi.models import Training

register = template.Library()

@register.assignment_tag(takes_context=True)
def next_training(context):
	request = context['request']
	training_list = Training.objects.filter(start__gte=datetime.date.today())[:5]
	return training_list

@register.filter
def remaining_seats(value):
	if (value.seats):
		if (value.occupied_seats):
			return value.seats - value.occupied_seats
		else :
			return value.seats
	else :
		return ""

@register.filter
def occupation_rate(value):
	if(value.seats):
		if (value.occupied_seats):
			return float(value.occupied_seats) / value.seats
		else:
			return 0
	else :
		return None

@register.filter
def rate_to_class(value):
	if(value):
		if(value<0.7):
			return "label-success"
		elif (value < 0.85):
			return "label-warning"
		else :
			return "label-danger"
	else :
		return "label-success"
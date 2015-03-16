from django import template

from aroe.models import *



register = template.Library()


# Retrieve the top menu of Association and describe the content of this menuitem
@register.assignment_tag(takes_context=True)
def association_menu(context):
	request = context['request']
	association_page_list = AssociationRootPage.objects.all()
	menuitems = []
	if len(association_page_list) == 1 :
		menuitems = AssociationTilePage.objects.live().descendant_of(association_page_list[0])
	return menuitems

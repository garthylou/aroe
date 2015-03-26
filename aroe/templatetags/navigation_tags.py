from django import template

from aroe.models import *



register = template.Library()


# Retrieve the top menu of Association and describe the content of this menuitem
@register.assignment_tag(takes_context=True)
def association_menu(context):
	request = context['request']
	association_page_list = AssociationRootPage.objects.live().all()
	menuitems = []
	if len(association_page_list) == 1 :
		menuitems = AssociationTilePage.objects.live().descendant_of(association_page_list[0])
	return menuitems

#Retrieve the top menu of Dossiers and describes the content of this menuitem
@register.assignment_tag(takes_context=True)
def dossier_menu(context):
	dossier_page = context['self']
	menuitems = []
	dossieritems = []
	if dossier_page :
		menuitems = ArticlePage.objects.live().descendant_of(dossier_page)
		dossieritems = DossierPage.objects.live().descendant_of(dossier_page)
		context['articleitems'] = menuitems
		context['dossieritems'] = dossieritems
	return menuitems


@register.assignment_tag(takes_context=True)
def article_menu(context):
	dossier_page = DossierPage.objects.live().ancestor_of(context['self']).first()
	context['dossier']=dossier_page
	menuitems = []
	dossieritems = []
	if dossier_page :
		menuitems = ArticlePage.objects.live().descendant_of(dossier_page)
		dossieritems = DossierPage.objects.live().descendant_of(dossier_page)
		context['articleitems'] = menuitems
		context['dossieritems'] = dossieritems
	return menuitems

@register.filter
def determine_dossier_class(value):
	if (value):
		if len(value) <= 12 :
			div = 12/len(value)
			return "col-md-%s col-lg-%s" % (div, div)
		else :
			return "col-md-12 col-lg-12"
	else :
		return ""
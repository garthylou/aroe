from django import template
import datetime

from aroe.models import *

register = template.Library()

@register.assignment_tag(takes_context=True)
def last_articles(context):
	articles_list = ArticlePage.objects.live().public().order_by("-latest_revision_created_at")[:4]
	return articles_list
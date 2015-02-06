from django.db import models

# Create your models here.
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailadmin.edit_handlers import FieldPanel, MultiFieldPanel, \
InlinePanel, PageChooserPanel
from modelcluster.fields import ParentalKey
from wagtail.wagtailsearch import index
from wagtail.wagtailimages.models import Image
from django.utils.translation import ugettext_lazy as _


# Carousel items
class CarouselItem(models.Model):
	image = models.ForeignKey(
		'wagtailimages.Image',
		null=True,
		blank=True,
		on_delete=models.SET_NULL,
		related_name='+',
		verbose_name=_('image')
	)
	caption = models.CharField(verbose_name=_("Title"), max_length=255, blank=True)
	panels = [
		ImageChooserPanel('image', ),
		FieldPanel('caption',),
	]
	class Meta:
		abstract = True

# Home page
class HomePage(Page):
    news = RichTextField(blank=True,verbose_name="News")
    search_fields = Page.search_fields + (
		index.SearchField('news'),
	)
    class Meta:
		verbose_name = _("Home")

class HomePageCarouselItem(Orderable, CarouselItem):
	page = ParentalKey('aroe.HomePage', related_name='carousel_items')


HomePage.content_panels = [
	FieldPanel('title', classname="full title"),
	FieldPanel('news', classname="full"),
	InlinePanel(HomePage, 'carousel_items', label="Carousel items"),
]


# AssociationRootPage
class AssociationRootPage(Page):
	subpage_types = ['aroe.AssociationTilePage']
	class Meta:
		verbose_name = _('Association')

class AssociationTilePage(Page):
	icon_class = models.CharField(verbose_name=_('Icon class'), max_length=255, blank=True)
	class Meta:
		verbose_name = _('Association tile')

AssociationTilePage.content_panels = [
	FieldPanel('title', classname="full title"),
	FieldPanel('icon_class', classname="full"),
]
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
	subpage_types = [
		'aroe.AssociationRootPage',
		'aroe.DossierPage',
		'aroe.SimplePage',
		'aroe.PressbookPage',
	]
	news = RichTextField(
		blank=True,
		verbose_name=_("News"),
		help_text=_("Text to put into the News part on Home."))
	search_fields = Page.search_fields + (
		index.SearchField('news'),
	)
	class Meta:
		verbose_name = _("Home")

class HomePageCarouselItem(Orderable, CarouselItem):
	page = ParentalKey('aroe.HomePage', related_name='carousel_items')


HomePage.content_panels = [
	FieldPanel('title', classname="full title"),
	FieldPanel('news', classname="full", ),
	InlinePanel(HomePage, 'carousel_items', label=_("Carousel items")),
]


# AssociationRootPage
class AssociationRootPage(Page):
	subpage_types = [
		'aroe.AssociationTilePage',
		'aroe.BureauPage',
		'aroe.MembresPage',
		'aroe.TrainingPage',
		'aroe.EmptyPage',
	]
	class Meta:
		verbose_name = _('Association')

class AssociationTilePage(Page):
	icon_class = models.CharField(verbose_name=_('Icon class'), max_length=255, blank=True, help_text=_("Text which represents icon from http://fontawesome.io/icons/"))
	class Meta:
		verbose_name = _('Association tile')

AssociationTilePage.content_panels = [
	FieldPanel('title', classname="full title"),
	FieldPanel('icon_class', classname="full"),
]

# BureauPage
class Poste(Orderable, models.Model):
	member = models.ForeignKey('aroeapi.Member', 
		null=True,
		blank=True,
		on_delete=models.SET_NULL,
		related_name='+',
		verbose_name=_('Member')
		)
	caption = models.CharField(verbose_name=_("Caption"), max_length=255, blank=True)
	panels = [
		FieldPanel('caption',),
		FieldPanel('member',)

	]
	page = ParentalKey('aroe.BureauPage', related_name='poste_items')



class BureauPage(AssociationTilePage):
	pass

BureauPage.content_panels = [
	FieldPanel('title', classname="full title"),
	FieldPanel('icon_class', classname="full"),
	InlinePanel(BureauPage, 'poste_items', label=_("Poste items")),
]

class MembresPage(AssociationTilePage):
	pass


class TrainingPage(AssociationTilePage):
	pass

class EmptyPage(AssociationTilePage):
	text = RichTextField(blank=False,verbose_name="Text",help_text=_("Text"))
	class Meta:
		verbose_name = _('Empty page')

EmptyPage.content_panels = [
	FieldPanel('title', classname="full title"),
	FieldPanel('icon_class', classname="full"),
	FieldPanel('text', classname="full"),
]


# Dossier and Article

class DossierImageItem(Orderable, models.Model):
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
	page = ParentalKey('aroe.DossierPage', related_name='image_items')

class DossierPage(Page):
	subpage_types = [
		'aroe.ArticlePage',
		'aroe.DossierPage'
	]
	text_content = RichTextField(blank=True,verbose_name=_("Introduction"),help_text=_("Introduce the content of the Dossier."))
	class Meta:
		verbose_name = _('Dossier')

DossierPage.content_panels = [
	FieldPanel('title', classname="full title"),
	FieldPanel('text_content', classname="full"),
	InlinePanel(DossierPage, 'image_items', label=_("Images")),
]

class ArticleImageItem(Orderable, models.Model):
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
	page = ParentalKey('aroe.ArticlePage', related_name='image_items')


class ArticlePage(Page):
	text_content = RichTextField(blank=True,verbose_name=_("Content"),help_text=_("Content of the article."))
	class Meta:
		verbose_name = _('Article')

ArticlePage.content_panels = [
	FieldPanel('title', classname="full title"),
	FieldPanel('text_content', classname="full"),
	InlinePanel(ArticlePage, 'image_items', label=_("Images")),
]


## Simple Page
class SimplePage(Page):
	text = RichTextField(blank=True,verbose_name="Text",help_text=_("Text"))
	class Meta:
		verbose_name = _('Simple page')

SimplePage.content_panels = [
	FieldPanel('title', classname="full title"),
	FieldPanel('text', classname="full"),
]

## PressBook Page
class PressbookPage(Page):
	subpage_types = [
		'aroe.PressbookArticlePage',
	]
	class Meta:
		verbose_name = _('Pressbook page')

class PressbookArticlePage(Page):
	text = RichTextField(blank=False,verbose_name=_("Text"),help_text=_("Text"))
	image = models.ForeignKey(
		'wagtailimages.Image',
		null=True,
		blank=True,
		on_delete=models.SET_NULL,
		related_name='+',
		verbose_name=_('image')
	)
	source = models.CharField(verbose_name=_("Source"), max_length=255,help_text=_("Title of the source"))
	detail = models.CharField(verbose_name=_("Source detail"), max_length=255, help_text=_("Detail of the source (publication date, # of the mag, ...)"))
	icon_source = models.ForeignKey(
		'wagtailimages.Image',
		null=True,
		blank=False,
		on_delete=models.SET_NULL,
		related_name='+',
		verbose_name=_('icon'),
		help_text=_('Icon of the source to display in pressbook.')
	)
	class Meta:
		verbose_name = _('article for pressbook')

PressbookArticlePage.content_panels = [
		FieldPanel('title', classname="full title"),
		ImageChooserPanel('icon_source',),
		FieldPanel('source', classname="full"),
		FieldPanel('detail', classname="full"),
		ImageChooserPanel('image', ),
		FieldPanel('text', classname="full"),

	]
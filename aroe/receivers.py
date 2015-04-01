from django.dispatch import receiver
from django.db.models.signals import post_save

from wagtail.wagtailimages.models import Image
from core.image_processing import ImageProcessor

import logging

logger = logging.getLogger(__name__)

@receiver(post_save, sender=Image)
def post_processing_image(sender, **kwargs):
	if kwargs['instance'].file :
		img_proc = ImageProcessor(kwargs['instance'].file.path)
		img_proc.auto_orient()
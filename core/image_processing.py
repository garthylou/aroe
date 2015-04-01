from PIL import Image, ExifTags
import os,sys

class ImageProcessor(object) :

	def __init__(self, image_path):
		self.image_path = image_path
		self.image = None

	def _open_image(self):
		self.image = Image.open(self.image_path)
		return self.image

	def auto_orient(self):
		if self.image is None :
			self.image = self._open_image()
		if hasattr(self.image, '_getexif'):
			for orientation in ExifTags.TAGS.keys():
				if ExifTags.TAGS[orientation]=='Orientation':
					break
        	e = self.image._getexif()       # returns None if no EXIF data
        	if e is not None:
        		exif=dict(e.items())
        		orientation = exif[orientation]
        		if orientation == 3: 
        			self.image = self.image.transpose(Image.ROTATE_180)
        		elif orientation == 6: 
        			self.image = self.image.transpose(Image.ROTATE_270)
        		elif orientation == 8: 
        			self.image = self.image.transpose(Image.ROTATE_90)
        		self.image.save(self.image_path)

	def resize(self, width, height) :
		if self.image is None :
			self.image = self._open_image()
		s = self.image.size
		ratio_width = s[0]/width
		ratio_height = s[1]/height
		if (ratio_width > 1 or ratio_height > 1):
			ratio = max(ratio_width, ratio_height)
			self.image = self.image.resize((int(s[0]/ratio), int(s[1]/ratio)),Image.ANTIALIAS)
			self.image.save(self.image_path)


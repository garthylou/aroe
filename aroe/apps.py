from django.apps import AppConfig
import watson

class AroeAppConfig(AppConfig):
	name = "aroe"
	def ready(self):
		HomePage = self.get_model("HomePage")
		EmptyPage = self.get_model("EmptyPage")
		DossierPage = self.get_model("DossierPage")
		ArticlePage = self.get_model("ArticlePage")
		SimplePage = self.get_model("SimplePage")
		PressbookPage = self.get_model("PressbookPage")
		PressbookArticlePage = self.get_model("PressbookArticlePage")

		watson.register(HomePage.objects.all())
		watson.register(EmptyPage.objects.all())
		watson.register(DossierPage.objects.all())
		watson.register(ArticlePage.objects.all())
		watson.register(SimplePage.objects.all())
		watson.register(PressbookPage.objects.all())
		watson.register(PressbookArticlePage.objects.all())

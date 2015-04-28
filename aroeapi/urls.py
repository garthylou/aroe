from rest_framework import routers
from aroeapi import views
from django.conf.urls import include,url

# Routers provide an easy way of automatically determining the URL conf
router_viewset = routers.SimpleRouter(trailing_slash=True)
router_viewset.register(r'members', views.MembersViewSet)
#router_viewset.register(r'avatars', views.AvatarMemberViewSet)
router_viewset.register(r'trainings', views.TrainingViewSet)

slashless_router = routers.SimpleRouter(trailing_slash=False)
slashless_router.registry = router_viewset.registry[:]

routerapi = [
	url(r'^', include(slashless_router.urls)),
	url(r'^', include(router_viewset.urls)),
	url(r'contact', views.send_message),
	]

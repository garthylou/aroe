from rest_framework import routers
from aroeapi import views
from django.conf.urls import include,url

# Routers provide an easy way of automatically determining the URL conf
router_viewset = routers.SimpleRouter(trailing_slash = False)
router_viewset.register(r'members', views.MembersViewSet)
router_viewset.register(r'avatars', views.AvatarMemberViewSet)
router_viewset.register(r'trainings', views.TrainingViewSet)

routerapi = [
	url(r'^', include(router_viewset.urls)),
	url(r'contact', views.send_message)
	]

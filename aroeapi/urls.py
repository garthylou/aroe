from rest_framework import routers
from aroeapi import views


# Routers provide an easy way of automatically determining the URL conf
routerapi = routers.SimpleRouter(trailing_slash = False)
routerapi.register(r'members', views.MembersViewSet)
routerapi.register(r'avatars', views.AvatarMemberViewSet)
routerapi.register(r'trainings', views.TrainingViewSet)

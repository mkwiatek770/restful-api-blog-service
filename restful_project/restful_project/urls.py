from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from users import views as user_views

router = routers.DefaultRouter()

router.register(r"users", user_views.UserViewSet)
router.register(r"groups", user_views.GroupViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("api_auth/", include("rest_framework.urls", namespace="rest_framework"))
]

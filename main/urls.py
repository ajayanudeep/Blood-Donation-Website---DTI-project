from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("display/", views.display, name="display"),
    path("create/", views.create, name="create"),
    path("myposts/",views.myposts,name="my posts")
]

from django.contrib import admin
from django.urls import base, path
from app1 import views
urlpatterns = [
    path("" , views.index, name="home"),
    path("about/" , views.about, name="about"),
    path("service/", views.services, name = "service"),
    path("contact", views.contact, name = "contact"),
    path("base/" , views.base, name = "base")
]


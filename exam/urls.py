from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
     path("", views.index, name="home"),
     path("about/", views.about, name="about123"),
     path("contact/", views.contact, name="contactus") ,
     path("jeetest/", views.jeetest, name="jeetest"),
     path("rejister/", views.rejister, name="rejister"),
     path("success/", views.success, name="success"),
     path("program/", views.program, name="program")
]
"""acoustid_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from acoustid_web.apps.main import views as main_views

urlpatterns = [
    path("", main_views.index, name="index"),
    path("about", main_views.about, name="about"),
    path("contact", main_views.contact, name="contact"),
    path("stats", main_views.stats, name="stats"),
    path("docs", main_views.docs, name="docs"),
    path("login", main_views.login, name="login"),
    path("admin/", admin.site.urls),
]

"""
URL configuration for project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from project import views

admin.autodiscover()

urlpatterns = [
    path("", views.HomepageView.as_view()),
    path("", include("django_prometheus.urls")),
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("app/", views.AppView.as_view(), name="dashboard"),
    path("healthz", views.HealthView.as_view(), name="healthz"),
]


if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()

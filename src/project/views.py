from django import http
from django.views.generic import TemplateView
from django.views.generic.base import View


class HealthView(View):
    def get(self, request, *args, **kwargs):
        return http.HttpResponse("OK", status=200)


class HomepageView(TemplateView):
    template_name = "homepage.html"


class AppView(TemplateView):
    template_name = "app.html"

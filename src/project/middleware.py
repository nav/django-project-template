from django.conf import settings
from django.contrib.auth.middleware import AuthenticationMiddleware
from django.shortcuts import redirect
from django.urls import NoReverseMatch, reverse


class LoginRequiredMiddleware(AuthenticationMiddleware):
    def process_view(self, request, view_func, view_args, view_kwargs):
        path = request.path
        if request.user.is_authenticated:
            return

        if path.startswith("/app"):
            try:
                login_url = reverse(settings.LOGIN_URL)
            except NoReverseMatch:
                login_url = settings.LOGIN_URL
            return redirect(f"{login_url}?next={path}")

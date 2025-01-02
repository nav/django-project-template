import logging

from django.http import HttpResponse

logger = logging.getLogger("project.tenant.middleware")


class HttpResponseServiceNotAvailable(HttpResponse):
    status_code = 503

from django.contrib.sessions.middleware import SessionMiddleware as BaseSessionMiddleware
from django.conf import settings


class SessionMiddleware(BaseSessionMiddleware):

    def process_response(self, request, response):
        response = super().process_response(request, response)
        try:
            if not request.user.is_authenticated:
                if response.cookies.get(settings.SESSION_COOKIE_NAME):
                    del response.cookies[settings.SESSION_COOKIE_NAME]
        except:
            pass
        return response


class MaintenanceMiddleware:
    """Serve a 503 "under maintenance" page for every request when settings.MAINTENANCE_MODE is on."""

    EXEMPT_PREFIXES = ("/admin/", "/static/", "/media/")

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if getattr(settings, "MAINTENANCE_MODE", False) and not request.path.startswith(self.EXEMPT_PREFIXES):
            from django.shortcuts import render
            response = render(request, "maintenance.html", status=503)
            response["Retry-After"] = "3600"
            return response
        return self.get_response(request)

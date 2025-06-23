from django.http import JsonResponse
from django.views.generic import TemplateView, CreateView

from .models import CallRequest


class IndexTemplateView(TemplateView):
    """Main landing page view."""

    template_name = "index.html"

class AboutTemplateView(TemplateView):
    """Main landing page view."""

    template_name = "about.html"


class CallRequestView(CreateView):
    """Handle call request submissions."""

    model = CallRequest
    http_method_names = ["post"]

    def post(self, request, *args, **kwargs):
        """Create a call request object and return a simple JSON response."""
        self.object = self.model.objects.create(
            fullname=request.POST.get("name", ""),
            phone_number=request.POST.get("phone", ""),
            comment=request.POST.get("comment", ""),
        )
        return JsonResponse({"status": "ok"})


class RobotsTxtView(TemplateView):
    """Serve robots.txt for crawlers."""

    template_name = "robots.txt"
    content_type = "text/plain"


class SitemapXmlView(TemplateView):
    """Serve sitemap.xml for crawlers."""

    template_name = "sitemap.xml"
    content_type = "text/xml"

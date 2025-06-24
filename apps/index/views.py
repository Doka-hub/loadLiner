from datetime import date

from django.http import JsonResponse
from django.views.generic import TemplateView, CreateView

from .models import CallRequest, ContactRequest


class IndexTemplateView(TemplateView):
    """Main landing page view."""

    template_name = "index.html"


class AboutTemplateView(TemplateView):
    template_name = "about.html"


class ContactTemplateView(TemplateView):
    template_name = "contact.html"


class ServiceTemplateView(TemplateView):
    template_name = 'services_transportation.html'

    def get_template_names(self):
        """Return the template name based on the service slug."""
        service_slug = self.kwargs.get("service_slug", "")
        print(service_slug)
        return [f"services_{service_slug}.html"] if service_slug else ["services/default.html"]


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


class ContactRequestView(CreateView):
    """Handle contact form submissions."""

    model = ContactRequest
    http_method_names = ["post"]

    def post(self, request, *args, **kwargs):
        start_date_str = request.POST.get("Anticipated Start Date")
        start_date = None
        if start_date_str:
            try:
                start_date = date.fromisoformat(start_date_str)
            except ValueError:
                start_date = None

        pallet_positions = request.POST.get("Pallet-Positions-Requested")
        if pallet_positions:
            try:
                pallet_positions = int(pallet_positions)
            except ValueError:
                pallet_positions = None

        self.object = self.model.objects.create(
            service=request.POST.get("Service", ""),
            full_name=request.POST.get("Full-name", ""),
            email=request.POST.get("Email-address", ""),
            phone_number=request.POST.get("Phone-number", ""),
            company_name=request.POST.get("Company-name", ""),
            markets_of_interest=request.POST.get("Markets-of-interest", ""),
            mode=request.POST.get("Mode", ""),
            industry=request.POST.get("Industry", ""),
            temperature_requirement=request.POST.get("Temperature-Requirement", ""),
            pallet_positions_requested=pallet_positions,
            anticipated_start_date=start_date,
            message=request.POST.get("Message", ""),
            how_did_you_hear_about_us=request.POST.get("How-did-you-hear-about-us", ""),
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

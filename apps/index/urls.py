from django.urls import path

from .views import (
    IndexTemplateView,
    PrivacyPolicyTemplateView,
    AboutTemplateView,
    ContactTemplateView,
    ServiceTemplateView,
    CallRequestView,
    ContactRequestView,
    RobotsTxtView,
    SitemapXmlView,
)

urlpatterns = [
    path("", IndexTemplateView.as_view(), name="index"),
    path("privacy-policy/", PrivacyPolicyTemplateView.as_view(), name="privacy_policy"),
    path("about/", AboutTemplateView.as_view(), name="about"),
    path("contact/", ContactTemplateView.as_view(), name="contact"),
    path("services/<service_slug>/", ServiceTemplateView.as_view(), name="services"),
    path("robots.txt", RobotsTxtView.as_view(), name="robots"),
    path("sitemap.xml", SitemapXmlView.as_view(), name="sitemap"),
    path("api/v1/call-me/", CallRequestView.as_view(), name="call_me"),
    path("api/v1/contact/", ContactRequestView.as_view(), name="contact_form"),
]

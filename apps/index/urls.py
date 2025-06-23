from django.urls import path

from .views import (
    IndexTemplateView,
    CallRequestView,
    RobotsTxtView,
    SitemapXmlView,
)

urlpatterns = [
    path("", IndexTemplateView.as_view()),
    path("robots.txt", RobotsTxtView.as_view(), name="robots"),
    path("sitemap.xml", SitemapXmlView.as_view(), name="sitemap"),
    path("api/v1/call-me/", CallRequestView.as_view(), name="call_me"),
]

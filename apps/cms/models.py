from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField


class HomePage(Page):
    body = RichTextField(blank=True)

    class Meta:
        verbose_name = "Home page"


class ContentPage(Page):
    body = RichTextField(blank=True)

    parent_page_types = ['cms.HomePage', 'cms.ContentPage']
    subpage_types = ['cms.ContentPage']

    class Meta:
        verbose_name = "Content page"

from wagtail.admin.panels.field_panel import FieldPanel
from wagtail.fields import RichTextField
from wagtail.models import Page


class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]

    class Meta:
        verbose_name = "Home page"


class ContentPage(Page):
    body = RichTextField(blank=True)

    parent_page_types = ['cms.HomePage', 'cms.ContentPage']
    subpage_types = ['cms.ContentPage']

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]

    class Meta:
        verbose_name = "Content page"

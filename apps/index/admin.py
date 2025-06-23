from django.contrib import admin

from .models import ContactRequest

@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):
    """Admin interface for ContactRequest model."""

    list_display = ('full_name', 'email', 'phone_number')
    search_fields = ('full_name', 'email', 'phone_number')
    list_filter = ('created',)
    ordering = ('-created',)

    def get_readonly_fields(self, request, obj=None):
        """Make all fields readonly in the admin interface."""
        return [field.name for field in self.model._meta.fields]
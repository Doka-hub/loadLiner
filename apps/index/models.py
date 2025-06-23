from django.db import models


class CallRequest(models.Model):
    fullname = models.CharField(max_length=255, verbose_name='Имя')
    phone_number = models.CharField(max_length=40, verbose_name='Телефон')
    comment = models.TextField(verbose_name='Комментарий')

    def __str__(self) -> str:
        return f"{self.fullname} ({self.phone_number})"

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'


class ContactRequest(models.Model):
    """Store submitted contact form data."""

    service = models.CharField(max_length=255, verbose_name="Сервис")
    full_name = models.CharField(max_length=255, verbose_name="Имя")
    email = models.EmailField(verbose_name="Email")
    phone_number = models.CharField(max_length=40, verbose_name="Телефон")
    company_name = models.CharField(max_length=255, verbose_name="Компания")
    markets_of_interest = models.CharField(
        max_length=255, blank=True, verbose_name="Market of interest"
    )
    mode = models.CharField(max_length=255, blank=True, verbose_name="Mode")
    industry = models.CharField(max_length=255, blank=True, verbose_name="Industry")
    temperature_requirement = models.CharField(
        max_length=255, blank=True, verbose_name="Temperature Requirement"
    )
    pallet_positions_requested = models.IntegerField(
        null=True, blank=True, verbose_name="Pallet Positions Requested"
    )
    anticipated_start_date = models.DateField(
        null=True, blank=True, verbose_name="Anticipated Start Date"
    )
    message = models.TextField(verbose_name="Message")
    how_did_you_hear_about_us = models.CharField(
        max_length=255, blank=True, verbose_name="How did you hear about us"
    )
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="Created"
    )
    updated = models.DateTimeField(auto_now=True, verbose_name="Updated")
    status = models.CharField(
        max_length=50, default="new", verbose_name="Status")

    def __str__(self) -> str:
        return f"{self.full_name} ({self.email})"

    class Meta:
        verbose_name = "Contact request"
        verbose_name_plural = "Contact requests"

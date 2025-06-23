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

from django.core.validators import MinLengthValidator
from django.db import models


class TgUser(models.Model):
    tg_chat_id = models.BigIntegerField(verbose_name="id чата")
    tg_user_ud = models.BigIntegerField(verbose_name="идентификатор пользователя")
    tg_username = models.CharField(max_length=32, validators=[MinLengthValidator(5)])
    user = models.ForeignKey("core.User", on_delete=models.CASCADE, null=True, blank=True, verbose_name="Пользователь")
    verification_code = models.CharField(max_length=10, null=True, blank=True, unique=True)

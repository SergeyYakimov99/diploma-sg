# Generated by Django 4.0.1 on 2022-12-21 17:38

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TgUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tg_chat_id', models.BigIntegerField(verbose_name='id чата')),
                ('tg_user_ud', models.BigIntegerField(verbose_name='идентификатор пользователя')),
                ('tg_username', models.CharField(max_length=32, validators=[django.core.validators.MinLengthValidator(5)])),
                ('verification_code', models.CharField(blank=True, max_length=10, null=True, unique=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
    ]

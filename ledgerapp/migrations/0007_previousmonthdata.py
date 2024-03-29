# Generated by Django 4.2 on 2024-03-09 14:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("ledgerapp", "0006_alter_bookmodel_user"),
    ]

    operations = [
        migrations.CreateModel(
            name="PreviousMonthData",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("income", models.IntegerField(blank=True, default=0, null=True)),
                ("expenses", models.IntegerField(blank=True, default=0, null=True)),
                ("month", models.DateField(unique=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]

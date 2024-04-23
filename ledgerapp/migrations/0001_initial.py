# Generated by Django 4.2 on 2024-03-03 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BookModel",
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
                ("title", models.CharField(max_length=100)),
                ("memo", models.TextField()),
                ("income", models.IntegerField()),
                ("expenses", models.IntegerField()),
                ("date", models.DateField()),
                ("sumincome", models.IntegerField()),
                ("sumexpenses", models.IntegerField()),
                ("kind", models.CharField(max_length=10)),
            ],
        ),
    ]
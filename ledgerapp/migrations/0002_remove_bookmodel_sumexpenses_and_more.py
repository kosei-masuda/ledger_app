# Generated by Django 4.2 on 2024-03-03 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ledgerapp", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="bookmodel", name="sumexpenses",),
        migrations.RemoveField(model_name="bookmodel", name="sumincome",),
        migrations.AlterField(
            model_name="bookmodel",
            name="memo",
            field=models.TextField(blank=True, default="", null=True),
        ),
    ]

# Generated by Django 4.2 on 2024-03-07 14:29

from django.db import migrations, models


def set_default_value(apps, schema_editor):
    BookModel = apps.get_model('ledgerapp', 'BookModel')
    for book in BookModel.objects.all():
        book.user = 'guest'
        book.save()
class Migration(migrations.Migration):

    dependencies = [
        ("ledgerapp", "0004_remove_bookmodel_sumexpenses_and_more"),
    ]

    operations = [
                migrations.AddField(
            model_name='bookmodel',
            name='user',
            field=models.CharField(default='temporary_value', max_length=100),  # ここに一時的なデフォルト値を設定する
            preserve_default=False,
        ),
        migrations.RunPython(set_default_value),
        migrations.AlterField(
            model_name='bookmodel',
            name='user',
            field=models.CharField(max_length=100),
        ),
    ]

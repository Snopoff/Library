# Generated by Django 3.1.2 on 2020-12-23 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lib', '0009_auto_20201223_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(blank=True, help_text='Brief description of the book'),
        ),
    ]

# Generated by Django 3.1.2 on 2020-12-23 10:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lib', '0006_auto_20201223_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='lib.genre'),
        ),
    ]
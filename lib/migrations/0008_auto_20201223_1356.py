# Generated by Django 3.1.2 on 2020-12-23 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lib', '0007_auto_20201223_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.ForeignKey(default='2947d6ee-b0bf-439e-b869-e8bff3415576', null=True, on_delete=django.db.models.deletion.SET_NULL, to='lib.genre'),
        ),
    ]

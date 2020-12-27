# Generated by Django 3.1.2 on 2020-12-27 20:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lib', '0010_auto_20201223_1359'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': 'Авторы'},
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['title', 'description'], 'verbose_name': 'Книги'},
        ),
        migrations.AlterModelOptions(
            name='genre',
            options={'verbose_name': 'Жанры'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Заказы'},
        ),
        migrations.AlterModelOptions(
            name='order_items',
            options={'verbose_name': 'Книги в заказе'},
        ),
    ]

# Generated by Django 3.1.2 on 2020-11-25 14:51

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this author across whole library', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('info', models.TextField(help_text='Brief information for this author')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this book across whole library', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(help_text='Brief description of the book')),
                ('publish_year', models.DateField(blank=True, null=True)),
                ('genre', models.CharField(max_length=100)),
                ('id_author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='lib.author')),
            ],
            options={
                'ordering': ['title', 'description'],
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for the staff person', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('sex', models.BooleanField(blank=True, null=True)),
                ('phone_number', models.CharField(max_length=11)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('position', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for the visitor', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=11)),
                ('email', models.CharField(max_length=100)),
                ('sex', models.BooleanField(blank=True, null=True)),
                ('birthday', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for given order', primary_key=True, serialize=False)),
                ('order_date', models.DateField(null=True)),
                ('id_staff', models.ForeignKey(help_text='Staff that made an order', null=True, on_delete=django.db.models.deletion.SET_NULL, to='lib.staff')),
                ('id_visitor', models.ForeignKey(help_text='Visitor that made an order', null=True, on_delete=django.db.models.deletion.SET_NULL, to='lib.visitor')),
            ],
        ),
        migrations.CreateModel(
            name='Order_Items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_book', models.ManyToManyField(help_text='Books in particular order', to='lib.Book')),
                ('id_orders', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='lib.orders')),
            ],
        ),
    ]

# Generated by Django 3.0.8 on 2021-02-17 08:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0005_auto_20210217_1104'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.RemoveField(
            model_name='sale',
            name='image',
        ),
    ]

# Generated by Django 3.0.8 on 2021-02-17 07:54

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0002_remove_product_item_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, default=0, max_length=255, null=True, verbose_name='image'),
        ),
    ]
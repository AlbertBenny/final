# Generated by Django 4.2.7 on 2023-12-04 04:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finalapp', '0004_rename_product_order_order_product'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Order',
        ),
    ]

# Generated by Django 4.2.7 on 2023-12-04 04:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finalapp', '0003_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='product',
            new_name='order_product',
        ),
    ]

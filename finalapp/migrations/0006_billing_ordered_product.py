# Generated by Django 4.2.7 on 2023-12-04 05:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finalapp', '0005_delete_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='billing',
            name='ordered_product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='finalapp.cart'),
        ),
    ]

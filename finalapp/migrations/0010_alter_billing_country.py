# Generated by Django 4.2.7 on 2023-12-06 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finalapp', '0009_remove_billing_product_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billing',
            name='country',
            field=models.CharField(choices=[('bangladesh', 'Bangladesh'), ('algeria', 'Algeria'), ('afghanistan', 'Afghanistan'), ('ghana', 'Ghana'), ('albania', 'Albania'), ('bahrain', 'Bahrain'), ('colombia', 'Colombia'), ('dominican Republic', 'Dominican Republic'), ('india', 'India')], max_length=20),
        ),
    ]

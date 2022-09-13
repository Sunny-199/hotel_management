# Generated by Django 4.0.6 on 2022-08-01 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_items_is_uploaded'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='disc_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=55, null=True),
        ),
        migrations.AlterField(
            model_name='items',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=55, null=True),
        ),
    ]
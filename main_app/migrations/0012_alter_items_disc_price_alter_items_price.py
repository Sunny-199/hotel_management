# Generated by Django 4.0.6 on 2022-08-03 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_items_hotel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='disc_price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='items',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

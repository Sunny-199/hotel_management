# Generated by Django 4.0.6 on 2022-08-18 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_promotions_hotel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='promotions',
            old_name='status',
            new_name='is_active',
        ),
    ]

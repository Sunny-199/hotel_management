# Generated by Django 4.0.6 on 2022-08-16 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0017_hotel_general_manager'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotel',
            name='general_manager',
        ),
    ]
# Generated by Django 4.0.6 on 2022-08-15 14:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0014_guests_hotem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='guests',
            old_name='hotem',
            new_name='hotel',
        ),
    ]

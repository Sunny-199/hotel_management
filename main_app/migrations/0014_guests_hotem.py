# Generated by Django 4.0.6 on 2022-08-15 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0013_room_menu_array'),
    ]

    operations = [
        migrations.AddField(
            model_name='guests',
            name='hotem',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.hotel'),
        ),
    ]
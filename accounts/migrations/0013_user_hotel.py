# Generated by Django 4.0.6 on 2022-08-15 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0013_room_menu_array'),
        ('accounts', '0012_role_hotel'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='hotel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_hotel', to='main_app.hotel'),
        ),
    ]

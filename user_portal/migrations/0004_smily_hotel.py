# Generated by Django 4.0.6 on 2022-09-08 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0020_hotel_payment_status'),
        ('user_portal', '0003_smily_remove_feedback_is_selected_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='smily',
            name='hotel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.hotel'),
        ),
    ]
# Generated by Django 4.0.6 on 2022-08-17 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_coupon_menu'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='max_discount',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

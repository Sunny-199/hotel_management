# Generated by Django 4.0.6 on 2022-09-08 12:46

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_portal', '0006_remove_smily_mood'),
    ]

    operations = [
        migrations.AddField(
            model_name='smily',
            name='mood',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=10, null=True), default=list, size=8),
        ),
    ]

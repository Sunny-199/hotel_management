# Generated by Django 4.0.6 on 2022-08-09 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_remove_role_permissions'),
    ]

    operations = [
        migrations.AddField(
            model_name='role',
            name='permissions',
            field=models.TextField(blank=True, null=True),
        ),
    ]

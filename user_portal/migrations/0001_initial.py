# Generated by Django 4.0.6 on 2022-09-07 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(blank=True, max_length=100, null=True)),
                ('mood', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]

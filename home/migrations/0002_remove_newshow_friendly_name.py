# Generated by Django 3.2.7 on 2022-11-26 08:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newshow',
            name='friendly_name',
        ),
    ]
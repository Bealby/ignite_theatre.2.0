# Generated by Django 3.2.7 on 2023-01-19 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0004_alter_ticket_web'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='show',
            name='poster',
        ),
    ]

# Generated by Django 3.2.7 on 2022-11-26 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20221126_1017'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='sponsor_url',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]

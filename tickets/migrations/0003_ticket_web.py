# Generated by Django 3.2.7 on 2022-11-18 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_auto_20221117_1206'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='web',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

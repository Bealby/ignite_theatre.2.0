# Generated by Django 3.2.7 on 2023-04-28 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0008_alter_show_poster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='location',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='position',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]

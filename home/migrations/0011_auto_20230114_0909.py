# Generated by Django 3.2.7 on 2023-01-14 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_show_sponsor_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='upcoming',
            old_name='address',
            new_name='location',
        ),
        migrations.AddField(
            model_name='upcoming',
            name='date',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='upcoming',
            name='position',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]

# Generated by Django 3.2.7 on 2022-11-26 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20221126_0920'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='New',
            new_name='NewShow',
        ),
        migrations.RenameModel(
            old_name='Upcoming',
            new_name='UpcomingShow',
        ),
    ]

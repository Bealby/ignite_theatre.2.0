# Generated by Django 3.2.7 on 2022-11-16 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cast', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='facebook',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]

# Generated by Django 3.2.7 on 2023-01-16 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='cast_show_link',
            field=models.CharField(default=0, max_length=254),
            preserve_default=False,
        ),
    ]

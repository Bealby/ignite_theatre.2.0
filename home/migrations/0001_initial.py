# Generated by Django 3.2.7 on 2022-11-26 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewShow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('image_ticket', models.ImageField(blank=True, null=True, upload_to='')),
                ('web_ticket', models.CharField(max_length=254)),
                ('address_ticket', models.CharField(max_length=254)),
                ('image_sponsor', models.ImageField(blank=True, null=True, upload_to='')),
                ('image_show', models.ImageField(blank=True, null=True, upload_to='')),
                ('content_show', models.TextField(max_length=254)),
                ('friendly_name', models.CharField(blank=True, max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UpcomingShow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('address', models.TextField(blank=True, null=True)),
            ],
        ),
    ]

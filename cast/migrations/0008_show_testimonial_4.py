# Generated by Django 3.2.7 on 2023-02-13 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cast', '0007_auto_20230202_0920'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='testimonial_4',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]

# Generated by Django 2.2 on 2020-04-09 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20200409_0956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='slug',
            field=models.SlugField(allow_unicode=True, blank=True, max_length=254, unique=True),
        ),
    ]

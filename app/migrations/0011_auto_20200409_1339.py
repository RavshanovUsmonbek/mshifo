# Generated by Django 2.2 on 2020-04-09 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20200409_1154'),
    ]

    operations = [
        migrations.RenameField(
            model_name='follower',
            old_name='emails',
            new_name='email',
        ),
    ]

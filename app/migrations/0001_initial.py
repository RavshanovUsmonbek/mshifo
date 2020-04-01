# Generated by Django 2.2 on 2020-04-01 11:14

import app.models
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('long', models.TextField()),
                ('lat', models.TextField()),
                ('address', models.CharField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, validators=[app.models.validate_name])),
                ('middle_name', models.CharField(blank=True, default=None, max_length=255, null=True, validators=[app.models.validate_name])),
                ('last_name', models.CharField(max_length=255, validators=[app.models.validate_name])),
                ('specialty', models.CharField(max_length=255)),
                ('bio', models.TextField()),
                ('image', models.ImageField(blank=True, height_field='height_field', null=True, upload_to='Doctors/', width_field='width_field')),
                ('width_field', models.IntegerField(default=0)),
                ('height_field', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Follower',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emails', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='HospitalInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('countent', tinymce.models.HTMLField()),
                ('year', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('num_staffs', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('num_awards', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('num_clients', models.PositiveSmallIntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'HospitalInfo',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, validators=[app.models.validate_name])),
                ('theme', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=254)),
                ('content', tinymce.models.HTMLField()),
                ('posted_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'News',
            },
        ),
        migrations.CreateModel(
            name='OpeningHour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weekday', models.IntegerField(choices=[(1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday'), (7, 'Sunday')], unique=True)),
                ('from_hour', models.TimeField()),
                ('to_hour', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=254, validators=[app.models.validate_name])),
                ('image', models.ImageField(blank=True, height_field='height_field', null=True, upload_to='ReviewsPic/', width_field='width_field')),
                ('width_field', models.IntegerField(default=0)),
                ('height_field', models.IntegerField(default=0)),
                ('content', tinymce.models.HTMLField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('short_description', tinymce.models.HTMLField()),
                ('is_top', models.BooleanField()),
                ('content', tinymce.models.HTMLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ServicePicture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, height_field='height_field', null=True, upload_to='ServicePic/', width_field='width_field')),
                ('width_field', models.IntegerField(default=0)),
                ('height_field', models.IntegerField(default=0)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='app.Service')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=254, validators=[app.models.validate_name])),
                ('email', models.EmailField(max_length=254)),
                ('content', models.TextField()),
                ('website', models.URLField()),
                ('news_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments_set', to='app.News')),
            ],
        ),
    ]

# Generated by Django 2.2 on 2020-02-21 11:40

import app.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('countent', models.TextField()),
                ('address', models.CharField(max_length=254)),
                ('email', models.EmailField(max_length=254)),
                ('estab_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Equipments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, height_field='height_field', null=True, upload_to=app.models.upload_location, width_field='width_field')),
                ('width_field', models.IntegerField(default=0)),
                ('height_field', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_menu', models.CharField(choices=[('F', 'footer'), ('T', 'topper')], max_length=1)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=254)),
                ('content', models.TextField()),
                ('comment_count', models.IntegerField()),
                ('posted_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=254)),
                ('image', models.ImageField(blank=True, height_field='height_field', null=True, upload_to=app.models.upload_location, width_field='width_field')),
                ('width_field', models.IntegerField(default=0)),
                ('height_field', models.IntegerField(default=0)),
                ('content', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('description', models.TextField()),
                ('picture', models.ImageField(upload_to=app.models.upload_location)),
                ('image', models.ImageField(blank=True, height_field='height_field', null=True, upload_to=app.models.upload_location, width_field='width_field')),
                ('width_field', models.IntegerField(default=0)),
                ('height_field', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=254)),
                ('email', models.EmailField(max_length=254)),
                ('content', models.TextField()),
                ('website', models.URLField()),
                ('news_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments_set', to='app.News')),
            ],
        ),
    ]

# Generated by Django 5.0.6 on 2024-05-15 16:21

import directory.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'platform',
                'verbose_name_plural': 'platforms',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'tag',
                'verbose_name_plural': 'tags',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reply_counts', models.IntegerField()),
                ('like_counts', models.IntegerField()),
                ('repost_counts', models.IntegerField()),
                ('source', models.URLField()),
                ('file', models.FileField(upload_to=directory.models.file_path_and_name)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('platform', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='directory.platform')),
                ('tags', models.ManyToManyField(to='directory.tag')),
            ],
            options={
                'verbose_name': 'video',
                'verbose_name_plural': 'videos',
                'ordering': ['-id'],
            },
        ),
    ]
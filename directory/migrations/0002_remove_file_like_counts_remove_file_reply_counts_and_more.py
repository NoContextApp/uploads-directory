# Generated by Django 5.0.6 on 2024-05-15 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='like_counts',
        ),
        migrations.RemoveField(
            model_name='file',
            name='reply_counts',
        ),
        migrations.RemoveField(
            model_name='file',
            name='repost_counts',
        ),
        migrations.AddField(
            model_name='file',
            name='comments_count',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='file',
            name='like_count',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='file',
            name='reply_count',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='file',
            name='repost_count',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='file',
            name='upvotes_count',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

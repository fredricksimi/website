# Generated by Django 3.0.7 on 2020-07-22 14:11

import ckeditor_uploader.fields
from django.db import migrations, models
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100)),
                ('authors_avatar', imagekit.models.fields.ProcessedImageField(blank=True, default='avatar.jpg', null=True, upload_to='profile_pics/')),
                ('title', models.CharField(db_index=True, max_length=100)),
                ('slug', models.SlugField(max_length=100)),
                ('author_twitter_link', models.CharField(blank=True, max_length=150, null=True)),
                ('author_linkedin_link', models.CharField(blank=True, max_length=150, null=True)),
                ('author_facebook_link', models.CharField(blank=True, max_length=150, null=True)),
                ('author_instagram_link', models.CharField(blank=True, max_length=150, null=True)),
                ('post_thumbnail', models.ImageField(upload_to='post_thumbnails/')),
                ('date_posted', models.DateField(auto_now_add=True)),
                ('body', ckeditor_uploader.fields.RichTextUploadingField()),
            ],
        ),
    ]

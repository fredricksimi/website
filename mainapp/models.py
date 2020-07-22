from django.db import models
from django.shortcuts import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

class BlogPost(models.Model):
    author = models.CharField(max_length=100)
    authors_avatar = ProcessedImageField(upload_to='profile_pics/',
                                    processors=[ResizeToFill(40,40)],
                                    format='JPEG',
                                    blank=True,null=True,
                                    default='avatar.jpg',
                                    options={'quality':90}
                                    )
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    # Authors Social Account Links
    author_twitter_link = models.CharField(max_length=150, blank=True, null=True)
    author_linkedin_link = models.CharField(max_length=150, blank=True, null=True)
    author_facebook_link = models.CharField(max_length=150, blank=True, null=True)
    author_instagram_link = models.CharField(max_length=150, blank=True, null=True)

    post_thumbnail = models.ImageField(upload_to='post_thumbnails/')
    date_posted = models.DateField(auto_now_add=True)
    body = RichTextUploadingField()
    

    def __str__(self):
        return f'{self.author} - {self.title} - {self.date_posted}'

    def get_absolute_url(self):
        return reverse('mainapp:blog-detail', kwargs={'slug':self.slug})
from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField

class Blog(models.Model):
    title = models.CharField(max_length=100,)
    date_posted = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField( blank=False, null=False)
    content= RichTextUploadingField()
    author = 'Eren Gul'

    def __str__(self):
        return self.title
from django.db import models
from django.utils.safestring import mark_safe
from ckeditor.fields import RichTextField
from django_ckeditor_5.fields import CKEditor5Field

class Blog(models.Model):
    title = models.CharField(max_length=100,)
    date_posted = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField( blank=True, null=True)
    content=CKEditor5Field('Text', config_name='extends')
    author = 'Eren Gul'

    def __str__(self):
        return self.title
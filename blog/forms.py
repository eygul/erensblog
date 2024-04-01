from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import Blog
class BlogForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Blog
        fields = '__all__'
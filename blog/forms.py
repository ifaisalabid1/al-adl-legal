from django import forms

from .models import BlogModel

from taggit.forms import TagField
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class BlogForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = BlogModel
        exclude = ()

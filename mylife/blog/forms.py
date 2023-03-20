from django import forms
from django.core.exceptions import ValidationError

from .models import Blog


class BlogModelForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
        labels = {'title': "Title"}, {'note': "Content of post"}

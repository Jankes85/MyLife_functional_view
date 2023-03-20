from django import forms
from django.core.exceptions import ValidationError

from .models import Blog

class DateInput(forms.DateInput):
    input_type = 'date'


class BlogModelForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
        labels = {'title': "Title"}, {'note': "Content of post"}
        widgets = {
            'entry_date': DateInput(attrs={'type': 'date'}),
        }

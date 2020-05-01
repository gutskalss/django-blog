from django import forms
from .models import Post
from django.utils.translation import ugettext_lazy as _


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'body', 'image']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-el title-input', 'placeholder': 'Введите название статьи'}),
            'body': forms.Textarea(attrs={'class': 'form-el body-input'}),
            'image': forms.FileInput(attrs={'class': 'form-el image-input'}),
        }

        labels = {
            'title': _(''),
            'body': _(''),
            'image': _(''),
        }

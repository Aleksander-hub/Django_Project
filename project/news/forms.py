# news/forms.py
from django import forms
from .models import Articles
from django.forms import ModelForm, TextInput, Textarea

class ArticlesForm(forms.ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'full_text', 'date', 'photo']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название статьи'}),
            'anons': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Анонс статьи'}),
            'full_text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Текст статьи'}),
            'date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
        }

# from tkinter import Widget
from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class ArticlesForm(ModelForm):

    class Meta:
        model = Articles# с какоу моделью мы работаем 
        fields = ['title','anons','full_text','date']# и с какими полями

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название новости'
                }), 
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс новости'
                }), 
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст новости'
                }), 
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                })
        }
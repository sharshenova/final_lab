from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    def clean(self):
        if not self.cleaned_data['text'] and not self.cleaned_data['image']:
            raise forms.ValidationError('Хотя бы одно из полей "Текст" и "Картинка" должно быть заполнено.')
        return super().clean()

    class Meta:
        model = Article
        fields = ['title', 'text', 'image']

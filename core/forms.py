from django import forms
from .models import Filme


class FilmeForm(forms.ModelForm):
    class Meta:
        model = Filme
        fields = '__all__'
        widgets = {
            'data_lancamento': forms.DateInput(attrs={'type': 'date'}),
            'sinopse': forms.Textarea(attrs={'rows': 4}),
        }

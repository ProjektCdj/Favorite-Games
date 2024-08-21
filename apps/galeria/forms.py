from django import forms
from apps.galeria.models import Thumb

class ThumbForms(forms.ModelForm):
    class Meta:
        model = Thumb
        exclude =  ['publicada' , ]
        labels = {
            'descricao': 'Descrição',
            'data_foto':'Data de Uplaod',
            'usuario': 'Usuário',
        }

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'plataforma': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'}),
            'foto': forms.FileInput(attrs={'class': 'form-control'}),
            'data_foto': forms.DateInput(
                format = '%d/%m/%Y',
                attrs={
                    'type': 'date',
                    'class': 'form-control'
                }
            ),
            'usuario': forms.Select(attrs={'class': 'form-control'}),
        }
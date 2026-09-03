from django import forms

from .models import Libro


class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'isbn', 'categoria', 'año_publicacion', 'cantidad_disponible']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Clean Code'}),
            'autor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Robert C. Martin'}),
            'isbn': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. 978-0132350884'}),
            'categoria': forms.Select(attrs={'class': 'form-select'}),
            'año_publicacion': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 2100}),
            'cantidad_disponible': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
        }

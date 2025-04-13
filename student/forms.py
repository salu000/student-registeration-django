from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['roll_no', 'name', 'age', 'std_class']
        widgets = {
            'roll_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'SXXBDOCS1M0XXXX'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter your age'}),
            'std_class': forms.Select(attrs={'class': 'form-control', 'placeholder': "Choose your section"}),
        }

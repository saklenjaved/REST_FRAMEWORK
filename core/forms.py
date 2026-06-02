from django import forms
from .models import Tasks, Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }

class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['title', 'category', 'completed', ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'completed': forms.CheckboxInput(),
            
        }

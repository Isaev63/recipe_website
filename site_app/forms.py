from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import RecipeModel


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class RecipeForm(forms.ModelForm):
    class Meta:
        model = RecipeModel
        fields = ['title', 'description', 'cooking_time', 'cooking_steps', 'image']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'cooking_steps': forms.Textarea(attrs={'rows': 4}),
        }

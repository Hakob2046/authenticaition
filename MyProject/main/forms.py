from django import forms
from .models import Messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class MessageModelForm(forms.ModelForm):
    class Meta:
        model=Messages
        fields='__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password1','password2']
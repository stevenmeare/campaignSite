# Custom forms file

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Extends the base UserCreationForm
class SignUpForm(UserCreationForm):
    # Includes first_name field
    first_name = forms.CharField(max_length=30, required=False)

    class Meta:
        model = User
        fields = ('username', 'first_name')
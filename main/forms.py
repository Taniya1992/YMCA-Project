from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

Position = [
    ('Staff User', 'Staff User'),
    ('Non Member', 'Non Member'),
    ('Ymca Member', 'Ymca Member'),
]

Gender = [
    ('Male', 'Male'),
    ('Female', 'Female'),
        ('Other', 'Other'),
]
class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30)
    Apply_for = forms.ChoiceField(choices=Position)
    Gender = forms.ChoiceField(choices=Gender)
    # Date_of_birth = forms.DateField()
    Contact_Number = forms.CharField(max_length=100)
    Address = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField(max_length=200)

    class Meta:
        model = User
        fields = ('username','Apply_for','Gender','Contact_Number','Address', 'email', 'password1', 'password2', )




 
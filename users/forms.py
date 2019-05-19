from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, CustomUsers

class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()
    # address = forms.CharField(max_length=50)
    # contact = forms.CharField()
    weight = forms.FloatField(label = 'Weight (in kg)')
    PACKAGE = (
        ('1', '1 Month'),
        ('3', '3 Months'),
        ('6', '6 Months'),
        ('12', '12 Months'),
    )
    package = forms.ChoiceField(choices=PACKAGE, required=True)
    class Meta:
        model = CustomUsers
        fields = ['username', 'first_name', 'last_name', 'email', 'address', 'contact', 'weight','package', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()
    address = forms.CharField(max_length=50)
    contact = forms.IntegerField()
    weight = forms.FloatField(label = 'Weight (in kg)')
    PACKAGE = (
        ('1', '1 Month'),
        ('3', '3 Months'),
        ('6', '6 Months'),
        ('12', '12 Months'),
    )
    package = forms.ChoiceField(choices=PACKAGE, required=True)


    class Meta:
        model = CustomUsers
        fields = ['username', 'first_name', 'last_name', 'email', 'address', 'contact', 'weight', 'package']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

# class RegistrationForm(forms.ModelForm):
#     class Meta:
#         model = Registration
#         fields = ['package', 'started_date']
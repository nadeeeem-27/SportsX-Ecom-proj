from django import forms
from django.contrib.auth.models import User
from .models import Customer

class UserInfoForm(forms.ModelForm):
    phone=forms.CharField( required=False,widget=forms.TextInput(attrs={'class': 'input', 'placeholder': "Phone"}) )
    address1=forms.CharField(  required=False,widget=forms.TextInput(attrs={'class': 'input', 'placeholder': "Address 1"}) )
    address2=forms.CharField(  required=False,widget=forms.TextInput(attrs={'class': 'input', 'placeholder': "Address 2"}) )
    city=forms.CharField(  required=False,widget=forms.TextInput(attrs={'class': 'input', 'placeholder': "City"}) )
    state=forms.CharField(  required=False,widget=forms.TextInput(attrs={'class': 'input', 'placeholder': "State"}) )
    zipcode=forms.CharField(  required=False,widget=forms.TextInput(attrs={'class': 'input', 'placeholder': "Zipcode"}))
    country=forms.CharField( required=False,widget=forms.TextInput(attrs={'class': 'input', 'placeholder': "Country"}) )

    class Meta:
        model = Customer
        fields = ['phone', 'address1', 'address2', 'city', 'state','zipcode','country']  # Include 'username' here


class RegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=150, required=True,widget=forms.TextInput(attrs={'class': 'input', 'placeholder': "username"}))  # Add the username field
    first_name = forms.CharField(max_length=30, required=True,widget=forms.TextInput(attrs={'class': 'input', 'placeholder': "first-name"}))
    last_name = forms.CharField(max_length=30, required=True,widget=forms.TextInput(attrs={'class': 'input', 'placeholder': "last-name"}))
    email = forms.EmailField(required=True,widget=forms.EmailInput(attrs={'class': 'input', 'placeholder': "Email"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': "password"}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': "confirm password"}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']  # Include 'username' here

    # Custom validation for confirming the passwords
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match each other.")

        return cleaned_data

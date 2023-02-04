from django import forms


class Login_form(forms.Form):
    login = forms.CharField(label="Login")
    password = forms.CharField(label="Password")

    
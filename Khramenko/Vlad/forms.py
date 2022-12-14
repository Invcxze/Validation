from django import forms
class UserForm(forms.Form):
    login = forms.CharField(widget=forms.TextInput(attrs={"class":"myfield"}),required=True, label="Логин")
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"myfield"}),required=True, label="Почта")
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"myfield"}),required=True, label="Пароль")
class UserSign(forms.Form):
    login = forms.CharField(widget=forms.TextInput(attrs={"class":"myfield"}),required=True, label="Логин")
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"myfield"}),required=True, label="Пароль")
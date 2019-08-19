from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(min_length=8, widget=forms.PasswordInput)


class RegisterForm(forms.ModelForm):

    password = forms.CharField(label="密码", 
                                min_length=6, 
                                max_length=20,
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label="确认密码", 
                                min_length=6, 
                                max_length=20,
                                widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ("username", "email")

    def confirm_password(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("密码不一致，请确认密码")
        return cd["password2"]
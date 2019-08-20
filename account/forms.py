from django import forms
from django.contrib.auth.models import User
from .models import Profile
from .models import Profile

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
    first_name = forms.CharField(label="first name", required=False)
    class Meta:
        model = User
        fields = ("username", "email")
    # 用clean_[fieldname] 来对字段进行验证，form.is_valid()调用时会检查这个函数
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("密码不一致，请确认密码")
        return cd["password2"]

    def clean_username(self):
        cd = self.cleaned_data
        username = cd['username']
        if len(username.replace(" ", "")) <= 3:
            raise forms.ValidationError("用户名不能少于三个非空白字符")
        elif r"./\|?<>,[]{!@#$%^&*}" in username:
            raise forms.ValidationErron("username有无效字符")
        else:
            return cd['username']

# 把Profile 模型拆分成 User Profile
class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")
        
# 可以不用在Profile中加上user，因为user是一个外键， 当然，也可以不用在写UserEditFrom,直接在视图函数里
# profile_form = ProfileForm(data=request.POST, files=request.FILES) 
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("profile_photo", "date_of_birth")
# 为什么要写成两个模型
from django import forms


class UserForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=128)
    password = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput)

class UserprofileForm(forms.Form):
    phonenumber=forms.CharField(label='电话', max_length=50)
    name = forms.CharField(label='姓名', max_length=128)

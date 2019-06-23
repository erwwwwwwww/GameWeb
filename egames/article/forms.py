from django import forms
from .models import Contact, UserModel, Comments
import re
from django.core.exceptions import ValidationError


# 验证手机格式
def mobileValidate(value):
    mobileRe = re.compile(r'^(13[0-9]|15[012356789]|17[678]|18[0-9]|14[57])[0-9]{8}$')
    if not mobileRe.match(value):
        raise ValidationError('手机号码格式错误')

# 留言表单
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'obj', 'text']
        widgets ={
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入名字'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': '请输入邮箱'}),
            'obj': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '主题'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': '内容', 'cols': '30', 'rows': '10'})

        }


# 注册表单
class RegisterForm(forms.Form):
    username = forms.CharField(max_length=20,
                               min_length=6,
                               label='用户名',
                               required=True,
                               error_messages={'required': '用户名不能为空', 'max_length': '用户名过长', 'min_length':'用户名过短'},
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入用户名6-20字符'}))
    password1 = forms.CharField(max_length=20,
                                min_length=6,
                                label='密码',
                                required=True,
                                error_messages={'required': '密码不能为空', 'max_length': '密码过长', 'min_length':'密码过短'},
                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '请输入密码6-20字符'}))
    password2= forms.CharField(max_length=20,
                               min_length=6,
                               label='密码',
                               required=True,
                               error_messages={'required': '密码不能为空', 'max_length': '密码过长', 'min_length':'密码过短'},
                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '请再次输入密码6-20字符'}))
    mobilePhone =forms.CharField(max_length=11,
                                 min_length=11,
                                 label='手机号码',
                                 required=True,
                                 validators=[mobileValidate,],
                                 error_messages={'required': '手机号码不能空', 'max_length': '请输入正确手机号码', 'min_length':'请输入正确手机号码'},
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'cols': '10', 'rows':'10',
                                                               'placeholder': '请输入11位数手机号码'}),
                                 help_text='手机号码', )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        userCount = len(UserModel.objects.filter(username=username))

        if userCount > 0:
            raise forms.ValidationError('账户已注册,请重新输入账户', code='invalid', params={'value': username})

        return username

    def clean(self):
        cleanedData = self.cleaned_data
        pwd = cleanedData['password1']
        pwd2 = cleanedData['password2']
        if pwd != pwd2:
            print(self.errors)
            raise forms.ValidationError('两次输入密码不一致', code='invalid', params={'value': pwd2})

        return cleanedData




# 登入表单
class LoginForm(forms.Form):
    username = forms.CharField(max_length=20,
                               label='用户',
                               error_messages={'required': '用户名不能为空'},
                               widget=forms.TextInput(attrs={'required': 'required', 'placeholder': '请输入账户名'}))
    password = forms.CharField(max_length=20,
                               label='密码',
                               error_messages={'required': '密码不能为空'},
                               widget=forms.PasswordInput(attrs={'required': 'required', 'placeholder': '请输入密码'}))


# 文章评论表单
class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['name', 'email', 'obj', 'body']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '输入名称'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': '请输入邮箱'}),
            'obj': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '主题'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': '内容', 'cols': '30', 'rows': '10'})

        }


























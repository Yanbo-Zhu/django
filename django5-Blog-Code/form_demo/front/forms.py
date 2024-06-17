from django import forms
from django.core import validators
from .models import Article

# 留言板的表单
class MessageBoardForm(forms.Form):
    title = forms.CharField(min_length=2, max_length=20, label='标题',
                            error_messages={
                                "min_length": '标题最小长度不能少于2！',
                                "max_length": "标题最大不能超过20！"
                            })
    content = forms.CharField(widget=forms.Textarea, label='内容')
    email = forms.EmailField(label='邮箱')



class RegisterForm(forms.Form):
    telephone = forms.CharField(validators=[validators.RegexValidator(r'1[345678]\d{9}', message='手机号码格式不符合！')])
    pwd1 = forms.CharField(min_length=6, max_length=100)
    pwd2 = forms.CharField(min_length=6, max_length=100)

    # clean_[field]
    def clean_telephone(self):
        telephone = self.cleaned_data.get('telephone')
        # 从数据库中查找telephone是否存在，如果存在，那么抛出验证错误
        if telephone == '18888888888':
            raise forms.ValidationError('手机号码已经存在！')
        else:
            return telephone

    def clean(self):
        cleaned_data = super().clean()
        pwd1 = cleaned_data.get('pwd1')
        pwd2 = cleaned_data.get('pwd2')
        if pwd1 != pwd2:
            raise forms.ValidationError("两次密码不一致！")
        else:
            return cleaned_data


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = "__all__"
        # fields = ['title', 'content']
        error_messages = {
            'category': {
                'required': 'category不能为空！'
            }
        }
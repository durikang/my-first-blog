from allauth.account.forms import SignupForm
from django import forms

class CustomSignupForm(SignupForm):
    email = forms.EmailField(max_length=254, label='이메일', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=30, label='아이디', widget=forms.TextInput(attrs={'pattern': '[a-zA-Z0-9]+', 'title': '영어와 숫자만 입력 가능합니다.', 'class': 'form-control'}))
    first_name = forms.CharField(max_length=30, label='이름', widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=30, label='성', widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    password1 = forms.CharField(
        max_length=30,
        label='비밀번호',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'required': 'required'}),
    )
    password2 = forms.CharField(
        max_length=30,
        label='비밀번호 확인',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'required': 'required'}),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'required': 'required'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'required': 'required'})

    def save(self, request):
        user = super().save(request)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.name = self.cleaned_data['first_name'] + self.cleaned_data['last_name']
        user.save()
        return user
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile


class CustomRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Ваш email")

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Пользователь с таким логином уже существует")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Пользователь с такой почтой уже существует")
        return email

class ProfileForm(forms.ModelForm):
    class Meta(UserCreationForm.Meta):
        model = Profile
        fields = ['telegram']

    def clean_telegram(self):
        telegram = self.cleaned_data.get('telegram')
        clean_tg = telegram.replace(' ', '').replace('-', '')

        if not clean_tg.startswith('@'):
            raise forms.ValidationError("Телеграм должен начинаться с @")

        return telegram
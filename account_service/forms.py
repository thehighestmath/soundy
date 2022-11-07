from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User

from account_service.models import CustomUser


class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = (
            'username',
            'first_name',
            'last_name',
            'tiktok_link',
        )
        labels = {
            'username': 'Логин',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'password1': 'Пароль',
            'password2': 'Подтвердите пароль',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        labels = {
            'username': 'Логин',
            'password1': 'Пароль',
            'password2': 'Подтвердите пароль',
        }
        for field_name in ['username', 'password1', 'password2']:
            self.fields[field_name].help_text = None
            self.fields[field_name].label = labels[field_name]

        self.helper = FormHelper()

        submit = Submit('button', 'Зарегистрироваться')
        submit.field_classes = 'btn btn-outline-primary btn-lg btn-block'
        self.helper.add_input(submit)


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['username'].label = "Логин"
        submit = Submit('button', 'Войти')
        submit.field_classes = 'btn btn-outline-primary btn-lg btn-block'
        self.helper.add_input(submit)


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = (
            'username',
            'first_name',
            'last_name',
            'tiktok_link',
        )


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = (
            'username',
            'first_name',
            'last_name',
            'tiktok_link',
        )

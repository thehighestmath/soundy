from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']
        labels = {
            'username': 'Логин',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
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

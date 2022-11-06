from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView

from .forms import RegisterForm, LoginForm


class RegisterView(CreateView):
    form_class = RegisterForm
    success_url = '/'
    template_name = 'account_service/register.html'

    def form_valid(self, form):
        form.save()
        return super(RegisterView, self).form_valid(form)


class MyLoginView(LoginView):
    redirect_authenticated_user = True
    form_class = LoginForm
    template_name = 'account_service/login.html'


class ProfileView(View):
    def get(self, request, **kwargs):
        return render(request, 'account_service/profile.html')

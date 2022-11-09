from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView
from django.views.generic import TemplateView

from .forms import LoginForm, BloggerSignUpForm, MusicianSignUpForm, BloggerViewForm, MusicianViewForm, BaseViewForm
from .models import CustomUser, Blogger, Musician


class CustomLoginView(LoginView):
    redirect_authenticated_user = True
    form_class = LoginForm
    template_name = 'account_service/login.html'


class ProfileView(View):
    def get(self, request, **kwargs):
        if request.user.is_blogger:
            blogger = Blogger.objects.get(user_id=request.user.id)
            base_form = BaseViewForm(instance=request.user)
            advanced_form = BloggerViewForm(instance=blogger)

        elif request.user.is_musician:
            musician = Musician.objects.get(user_id=request.user.id)
            base_form = BaseViewForm(instance=request.user)
            advanced_form = MusicianViewForm(instance=musician)

        else:
            base_form = BaseViewForm(instance=request.user)
            advanced_form = None

        return render(request, 'account_service/profile.html', {
            'base_form': base_form,
            'advanced_form': advanced_form,
        })


class SignUpView(TemplateView):
    template_name = 'account_service/signup.html'


class BloggerSignUpView(CreateView):
    model = CustomUser
    form_class = BloggerSignUpForm
    template_name = 'account_service/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'блоггер'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('profile')


class MusicianSignUpView(CreateView):
    model = CustomUser
    form_class = MusicianSignUpForm
    template_name = 'account_service/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'музыкант'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('profile')

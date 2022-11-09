from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import *

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('signup/', SignUpView.as_view(), name='signup'),
    path('signup/blogger/', BloggerSignUpView.as_view(), name='blogger_signup'),
    path('signup/musician/', MusicianSignUpView.as_view(), name='musician_signup'),

    path('profile/', ProfileView.as_view(), name='profile'),
]

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from .forms import UserCreateForm


# Create your views here.


class HomePageView(TemplateView):
    template_name = 'homePage.html'


class SignUpCreateView(CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

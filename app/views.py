from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, TemplateView, ListView
from .forms import UserCreateForm
from .models import PagesModel


# Create your views here.

class IndexPage(TemplateView):
    template_name = 'index.html'


class SignUpCreateView(CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class PagesDetailView(DetailView):
    template_name = 'homePage.html'
    model = PagesModel


class PagesListView(ListView):
    template_name = 'baseNav.html.html'
    model = PagesModel

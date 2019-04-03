from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, TemplateView
from .forms import UserCreateForm
from .models import PagesModel


# Create your views here.

def home_page(request):
    return redirect('homepage', pk=1)


class SignUpCreateView(CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class PagesDetailView(DetailView):
    template_name = 'index.html'
    model = PagesModel

    def get_context_data(self, **kwargs):
        contenxt = super(PagesDetailView, self).get_context_data(**kwargs)
        contenxt['object_list'] = PagesModel.objects.all()
        return contenxt

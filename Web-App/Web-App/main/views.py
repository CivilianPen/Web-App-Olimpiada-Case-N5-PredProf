from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import CreateView

from .forms import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from .utils import *

def ApplicationsForm(request):
    if request.method == 'POST':
        form = AddPostFormR(request.POST or None, user=request.user)
        if form.is_valid():
            try:
                Applications.objects.create(**form.cleaned_data)
                return  redirect('application')
            except:
                form.add_error(None,'Ошибка')
    else:
        form=AddPostFormR(user=request.user)

    r = list(Applications.objects.all())
    return render(request, 'main/Application.html' , {'form': form ,'r' : r})

def page(request):
    Items = list(Goods.objects.all())
    return render(request, 'main/index.html' , {'Items': Items})


class RegisterUser(DataMixin, CreateView):
    form_class = UserCreationForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('main')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'main/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('main')



def logout_user(request):
    logout(request)
    return redirect('login')


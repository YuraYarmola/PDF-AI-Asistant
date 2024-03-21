from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView, View
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .models import Profile
from main.models import UploadedFile
from .forms import *
class UserListView(ListView):
    model = Profile
    template_name = 'user_list.html'


class UserCreateView(CreateView):
    model = Profile
    form_class = UserForm
    success_url = reverse_lazy('user_list')
    template_name = 'user_form.html'


class UserProfileView(View):
    def get(self, request, *args, **kwargs):
        user = Profile.objects.get(pk=kwargs.get('pk'))
        files = UploadedFile.objects.filter(user=user)
        template_name = 'user_profile.html'
        return render(request, template_name, {'user': user , 'files': files})


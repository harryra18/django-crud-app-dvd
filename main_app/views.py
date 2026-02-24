from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpResponseForbidden

from .models import DVD, Genre
from .forms import SignUpForm, DVDForm
from .utils import fetch_movie_image


def home(request):
    return render(request, 'home.html')


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dvd-index')
        else:
            error_message = "Invalid sign up"
    form = SignUpForm()
    return render(request, 'registration/signup.html', {
        'form': form,
        'error_message': error_message
    })



class GenreList(LoginRequiredMixin, ListView):
    model = Genre
    template_name = 'main_app/genre_list.html'


class GenreDetail(LoginRequiredMixin, DetailView):
    model = Genre
    template_name = 'main_app/genre_detail.html'



class DVDList(LoginRequiredMixin, ListView):
    model = DVD
    template_name = 'main_app/dvd_list.html'

    def get_queryset(self):
        return DVD.objects.filter(user=self.request.user)


class DVDDetail(LoginRequiredMixin, DetailView):
    model = DVD
    template_name = 'main_app/dvd_detail.html'

    def get_queryset(self):
        return DVD.objects.filter(user=self.request.user)


class DVDCreate(LoginRequiredMixin, CreateView):
    model = DVD
    form_class = DVDForm
    template_name = 'main_app/dvd_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user

        image_url = fetch_movie_image(form.instance.title)
        if image_url:
            form.instance.image_url = image_url

        return super().form_valid(form)


class DVDUpdate(LoginRequiredMixin, UpdateView):
    model = DVD
    form_class = DVDForm
    template_name = 'main_app/dvd_form.html'

    def get_queryset(self):
        return DVD.objects.filter(user=self.request.user)


class DVDDelete(LoginRequiredMixin, DeleteView):
    model = DVD
    success_url = reverse_lazy('dvd-index')

    def get_queryset(self):
        return DVD.objects.filter(user=self.request.user)
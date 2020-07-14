from django.shortcuts import render
from django.views.generic import ListView, DeleteView, CreateView, UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Announcement


# Create your views here.
# Template Name = <app>/<model>_<viewtype>.html
class AnnouncementsListView(LoginRequiredMixin, ListView):
    model = Announcement


class AnnouncementsDetailView(LoginRequiredMixin, DetailView):
    model = Announcement


class AnnouncementsCreateView(LoginRequiredMixin, CreateView):
    model = Announcement
    fields = ['title', 'content', 'date_posted']
    success_url = '/user/announcement/'


class AnnouncementsDeleteView(LoginRequiredMixin, DeleteView):
    model = Announcement
    success_url = '/user/announcement'


class AnnouncementsUpdateView(LoginRequiredMixin, UpdateView):
    model = Announcement
    fields = ['title', 'content', 'date_posted']
    success_url = '/user/announcement'

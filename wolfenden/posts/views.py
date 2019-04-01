from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import Urban, Nature, Portrait


class UrbanPageView(ListView):
    model = Urban
    template_name = 'den/urban.html'

class NaturePageView(ListView):
    model = Nature
    template_name = 'den/nature.html'

class PortraitPageView(ListView):
    model = Portrait
    template_name = 'den/portrait.html'

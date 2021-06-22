from django.shortcuts import render
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = "home.html"

class LogIn(TemplateView):
    template_name = "login.html"
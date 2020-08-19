from django.shortcuts import render
from django.views import generic
from django.views.generic.base import TemplateView
from .models import *

class IndexView(TemplateView):
    template_name = "core/index.html"

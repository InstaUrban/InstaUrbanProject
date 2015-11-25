from django.shortcuts import render
from images.models import Image
from django.views.generic import TemplateView, ListView, DetailView


class ListImage(ListView):
    model = Image
    template_name = "image_list.html"

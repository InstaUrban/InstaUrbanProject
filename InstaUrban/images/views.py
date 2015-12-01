from django.shortcuts import render
from images.models import Image
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User


class ListImage(ListView):
    model = Image
    template_name = "image_list.html"

    def dispatch(self, request, *args, **kwargs):
        self.queryset = Image.objects.all().order_by('created')[::-1]
        return super(ListImage, self).dispatch(request, *args, **kwargs)


class ImageDetail(DetailView):
    model = Image
    template_name = "image_detail.html"

    def get_context_data(self, **kwargs):
        context = super(ImageDetail, self).get_context_data(**kwargs)
        return context


class ListMap(ListView):
    model = Image
    template_name = "map.html"

    def dispatch(self, request, *args, **kwargs):
        self.queryset = Image.objects.all().order_by('created')[::-1]
        return super(ListMap, self).dispatch(request, *args, **kwargs)


class CreateImage(CreateView):
    model = Image
    template_name = "image_form.html"
    fields = ['name',
              'image',
              'description',
              'city',
              'location', ]

    success_url = '/list_place'

    @method_decorator(login_required(login_url="/signin/"))
    def dispatch(self, *args, **kwargs):
        return super(CreateImage, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        user_django = User.objects.get(id=self.request.user.id)
        form.instance.owner = user_django
        return super(CreateImage, self).form_valid(form)

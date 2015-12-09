from django.shortcuts import render
from images.models import Image
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger


class ListImage(ListView):
    model = Image
    template_name = "image_list.html"
    paginate_by = 6

    def dispatch(self, request, *args, **kwargs):
        self.queryset = Image.objects.all().order_by('created')[::-1]
        return super(ListImage, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ListImage, self).get_context_data(**kwargs)
        list_image = Image.objects.all()
        paginator = Paginator(list_image, self.paginate_by)

        page = self.request.GET.get('page')

        try:
            file_image = paginator.page(page)
        except PageNotAnInteger:
            file_image = paginator.page(1)
        except EmptyPage:
            file_image = paginator.page(paginator.num_pages)

        context['list_image'] = file_image
        return context


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

    success_url = '/list_image'

    @method_decorator(login_required(login_url="/"))
    def dispatch(self, *args, **kwargs):
        return super(CreateImage, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        user_django = User.objects.get(id=self.request.user.id)
        form.instance.owner = user_django
        return super(CreateImage, self).form_valid(form)


class IndexView(TemplateView):
    template_name = "index.html"

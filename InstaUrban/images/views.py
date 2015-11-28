from django.shortcuts import render
from images.models import Image
from django.views.generic import TemplateView, ListView, DetailView


def mapa2(request):
    return render(request, 'mapgeoloc.html')


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

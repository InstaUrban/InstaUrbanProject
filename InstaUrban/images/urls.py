from django.conf.urls import url
from images.views import ListImage, ListMap, ImageDetail

urlpatterns = [

    url(r'^list_image/',
        ListImage.as_view(),
        name='home'),

    url(r'^image_detail/(?P<pk>[0-9]+)',
        ImageDetail.as_view(),
        name='image_detail'),

    url(r'^map/',
        ListMap.as_view(),
        name='map'),
    url(r'^mapa$', 'images.views.mapa2', name="mapa"),
]

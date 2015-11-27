from django.conf.urls import url
from images.views import ListImage, ListMap

urlpatterns = [

    url(r'^list_image/',
        ListImage.as_view(),
        name='home'),
    url(r'^map/',
        ListMap.as_view(),
        name='map'),
]

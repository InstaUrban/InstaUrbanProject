from django.conf.urls import url
from images.views import ListImage

urlpatterns = [

    url(r'^list_image/',
        ListImage.as_view(),
        name='home'),
]

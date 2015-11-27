from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from InstaUrban import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url('', include('images.urls', namespace='images')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

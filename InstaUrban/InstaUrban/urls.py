from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from InstaUrban import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url('', include('users.urls', namespace='users')),
    url('', include('images.urls', namespace='images')),
    url('', include('social.apps.django_app.urls', namespace='social')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

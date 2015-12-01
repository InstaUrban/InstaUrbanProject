from django.conf.urls import include, url
from users.views import UserLogin, UserCreate

urlpatterns = [

    url(r'^login/$',
        UserLogin.as_view(),
        name='sigin'),
    url(r'^signup/$',
        UserCreate.as_view(),
        name='signup'),
    url(r'^logout/$', 'users.views.logout_view', name='logout'),

]

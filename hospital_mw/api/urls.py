from django.conf.urls import url
from . import views

urlpatterns = [
    # ex: /api/
    url(r'^$', views.index, name='index'),
    # ex: /api/user/:user_id/
    url(r'^user/(?P<user_id>[0-9]+)/$', views.user, name='user'),
]

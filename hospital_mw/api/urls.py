from django.conf.urls import url
from . import views

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'user/(?P<user_id>[0-9]+)/$', views.user, name='user'),
]

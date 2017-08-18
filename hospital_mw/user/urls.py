from django.conf.urls import url
from . import views

urlpatterns = [
    # ex: /user/
    url(r'^$', views.index, name='index'),
]

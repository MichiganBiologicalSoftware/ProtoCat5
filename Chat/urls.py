"""Define the acceptable URLs for chat."""

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index')
]

"""Define the acceptable URLs for miscellaneous pages."""

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index')
]

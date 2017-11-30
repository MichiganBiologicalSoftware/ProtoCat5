"""Define the acceptable URLs for /api/user."""

from django.conf.urls import url
from . import api_views

urlpatterns = [
    url(r'$', api_views.index, name='index')
]

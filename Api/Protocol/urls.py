"""Define the acceptable URLs for /api/protocol."""

from django.conf.urls import url
from . import api_views

urlpatterns = [
    url(r'^(?P<protocol_id>[0-9]*)/?$', api_views.index, name='index')
]

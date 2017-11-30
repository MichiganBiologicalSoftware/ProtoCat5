"""Define the acceptable URLs for API."""

from django.conf.urls import include, url

urlpatterns = [
    url(r'chat/', include('Api.Chat.urls')),
    url(r'favorite/', include('Api.Favorite.urls')),
    url(r'group/', include('Api.Group.urls')),
    url(r'protocol/', include('Api.Protocol.urls')),
    url(r'user/', include('Api.User.urls')),
]

"""Define the acceptable URLs for groups."""

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^group/$', views.group, name="group_index_page"),
	url(r'^group/(?P<group_id>[0-9]+)$', views.protocol_by_group, name="group_protocol_page"),
	url(r'^submitgroupprotocol/$', views.add_group_protocol, name="group_protocol__add_page"),
	url(r'^deletegroupprotocol/$', views.delete_group_protocol, name="group_protocol__delete_page"),
    url(r'^groupsignup/$', views.group_signup, name="groupsignup"),
]

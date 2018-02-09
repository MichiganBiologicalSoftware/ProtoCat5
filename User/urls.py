"""Define the acceptable URLs for users."""

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login_user, name="login_page"),
    url(r'^submitlogin/$', views.submit_login, name="submit_login_page"),
    url(r'^signup/$', views.sign_up, name="sign_up_page"),
    url(r'^submitsignup/$', views.submit_sign_up, name="submit_page"),
    url(r'^logout/$', views.logoff, name="logoff"),
    url(r'^(?P<user_id>[0-9]+)/$', views.user, name="user_page")
]

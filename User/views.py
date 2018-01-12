"""Define the basic views for users."""

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    """User index page."""
    return HttpResponse("Testing")


def login_user(request):
	current_profile_info = request.user
	if (not current_profile_info.is_anonymous()):
		current_profile_info = ProfileInfo.objects.get(user = current_profile_info)
	else:
		current_profile_info = None
	context = {
		'title': 'ProtoCat - Login',
		'current_profile_info': current_profile_info,
	}
	return render(request, 'login.html', context)

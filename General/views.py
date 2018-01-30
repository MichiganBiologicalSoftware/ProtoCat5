"""Define the basic views for miscellaneous pages."""

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
	context = {
		'title': 'ProtoCat5.0',
		'current_profile_info': current_profile_info,
	}
	return render(request, 'index.html', context)
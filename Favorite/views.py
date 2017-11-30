"""Define the basic views for favorite."""

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    """Favorite index page."""
    return HttpResponse("Testing")

"""Define the API for favorites."""

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    """Favorites API index page."""
    return HttpResponse("Testing")

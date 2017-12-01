"""Define the basic views for search."""

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    """Search index page."""
    return HttpResponse("Testing")

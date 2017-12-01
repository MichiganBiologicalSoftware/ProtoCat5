"""Define the API for users."""

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    """User API index page."""
    return HttpResponse("Testing")

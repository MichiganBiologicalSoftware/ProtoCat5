"""Define the basic views for users."""

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    """User index page."""
    return HttpResponse("Testing")

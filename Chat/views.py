"""Define the basic views for chat."""

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    """Chat index page."""
    return HttpResponse("Testing")

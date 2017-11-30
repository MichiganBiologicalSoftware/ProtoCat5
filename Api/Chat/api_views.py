"""Define the API for chat."""

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    """Group index page."""
    return HttpResponse("Testing")

"""Define the API for protocols."""

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    """Protocol API index page."""
    return HttpResponse("Testing")

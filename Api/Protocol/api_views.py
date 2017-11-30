"""Define the API for protocols."""

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    """Group index page."""
    return HttpResponse("Testing")

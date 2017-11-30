"""Define the basic views for protocols."""

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    """Protocol index page."""
    return HttpResponse("Testing")

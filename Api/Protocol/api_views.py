"""Define the API for protocols."""

from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render

from Protocol.models import Protocol

def index(request, protocol_id=None):
    """Protocol API index page."""
    try:
        protocol = Protocol.objects.get(id=protocol_id)
    except Exception:
        # Make a 404 Exception
        return JsonResponse({"err_msg":"ERROR!"})

    response = {}
    response["id"] = protocol.id

    return JsonResponse(response)

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
    response["title"] = protocol.title
    response["description"] = protocol.description
    response["author"] = protocol.author.user.username
    response["materials"] = protocol.materials

    response["steps"] = []
    for step in protocol.steps.all():
        step_dict = {}
        step_dict["number"] = step.number
        step_dict["content"] = step.content
        response["steps"].append(step_dict)

    return JsonResponse(response)

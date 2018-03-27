"""Define the API for favorites."""

from django.http import HttpResponse, JsonResponse
from User.models import UserInfo
from django.shortcuts import render
from django.core import serializers

def index(request):
    """Favorites API index page."""
    query = request.GET.get("q", "")
    
    users = UserInfo.objects.filter(about__contains=query)
    match_users = []
    for user in users:
        match_users.append(user.user.username)

    return JsonResponse({
        "query": query,
        "users": match_users
    })

"""Define the API for favorites."""

from django.http import HttpResponse, JsonResponse
from User.models import UserInfo
from django.shortcuts import render
from django.core import serializers

def index(request):
    """Favorites API index page."""
    query = request.GET.get("q", "")
    match_users = []

    if not query:
        return JsonResponse({
            "query": query,
            "users": match_users
        })

    query_words = query.split()

    users = UserInfo.objects.filter(about__icontains=query_words[0])
    users = users | UserInfo.objects.filter(user__username__icontains=query_words[0])
    users = users | UserInfo.objects.filter(user__email__icontains=query_words[0])
    users = users | UserInfo.objects.filter(user__first_name__icontains=query_words[0])
    users = users | UserInfo.objects.filter(user__last_name__icontains=query_words[0])

    for word in query_words[1:]:
        users = users | UserInfo.objects.filter(about__icontains=word)
        users = users | UserInfo.objects.filter(user__username__icontains=word)
        users = users | UserInfo.objects.filter(user__email__icontains=word)
        users = users | UserInfo.objects.filter(user__first_name__icontains=word)
        users = users | UserInfo.objects.filter(user__last_name__icontains=word)

    for user in users:
        match_users.append(user.user.username)

    return JsonResponse({
        "query": query,
        "users": match_users
    })

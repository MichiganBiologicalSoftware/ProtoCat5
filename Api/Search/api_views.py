"""Define the API for favorites."""

from django.http import HttpResponse, JsonResponse
from User.models import UserInfo
from Protocol.models import Protocol
from django.shortcuts import render
from django.core import serializers

def index(request):
    """Favorites API index page."""
    query = request.GET.get("q", "")
    match_users = []
    match_protocols = []

    if not query:
        return JsonResponse({
            "query": query,
            "users": match_users,
            "protocols": match_protocols
        })

    query_words = query.split()

    users = UserInfo.objects.filter(about__icontains=query_words[0])
    users = users | UserInfo.objects.filter(user__username__icontains=query_words[0])
    users = users | UserInfo.objects.filter(user__first_name__icontains=query_words[0])
    users = users | UserInfo.objects.filter(user__last_name__icontains=query_words[0])

    for word in query_words[1:]:
        users = users | UserInfo.objects.filter(about__icontains=word)
        users = users | UserInfo.objects.filter(user__username__icontains=word)
        users = users | UserInfo.objects.filter(user__first_name__icontains=word)
        users = users | UserInfo.objects.filter(user__last_name__icontains=word)

    for user in users:
        match_users.append(user.user.username)

    for protocol in helper_search_protocol(query_words):
        match_protocols.append(protocol.id)

    return JsonResponse({
        "query": query,
        "users": match_users,
        "protocols": match_protocols
    })

def helper_search_protocol(query_words):
    """Search the protocols for the query words."""
    protocols = Protocol.objects.filter(title__icontains=query_words[0])
    protocols = protocols | Protocol.objects.filter(description__icontains=query_words[0])
    protocols = protocols | Protocol.objects.filter(materials__icontains=query_words[0])
    protocols = protocols | Protocol.objects.filter(steps__content__icontains=query_words[0])

    for word in query_words[1:]:
        protocols = Protocol.objects.filter(title__icontains=word)
        protocols = protocols | Protocol.objects.filter(description__icontains=word)
        protocols = protocols | Protocol.objects.filter(materials__icontains=word)
        protocols = protocols | Protocol.objects.filter(steps__content__icontains=word)

    return protocols    

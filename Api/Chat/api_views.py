"""Define the API for chat."""

from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseForbidden

def index(request):
    """Chat API index page."""
    if request.method == "POST":
		post(request)
    if request.method == "GET":
		get(request)
    if request.method == "DELETE":
		delete(request)
    return HttpResponse("Testing")

def post(request):
	for key in request.POST:
		if key[:5] == 'check':
			id = key[5:]
			tempMessage = models.Message.objects.get(id=id)
			tempMessage.deleted = True
			tempMessage.save()

def get(request):
	if request.user.is_anonymous():
		return HttpResponseForbidden()
	else:
		user = ProfileInfo.objects.get(user = request.user)

	messages = models.Message.objects.filter(recipient=user).filter(deleted=False).order_by('-timeSent')

	for message in messages:
		message.read = True
		message.save()

	context = {
		'title': 'Inbox',
		'message_list': messages,
	}
	if (request.user.is_anonymous()):
		context['current_profile_info'] = None
	else:
		context['current_profile_info'] = request.user.profileinfo
	return context

def delete(request):
	if request.user.is_anonymous():
		return HttpResponseForbidden()
	else:
		user = ProfileInfo.objects.get(user = request.user)
	message_id = request.args['id']
	message = models.Message.objects.filter(recipient=user).filter(id=message_id)
	message.deleted = True
	message.save()

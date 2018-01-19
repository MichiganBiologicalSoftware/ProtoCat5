"""Define the API for chat."""

from django.http import HttpResponse
from django.shortcuts import render

def inbox_view(request):
	if request.method == "POST":
		for key in request.POST:
			if key[:5] == 'check':
				id = key[5:]
				tempMessage = models.Message.objects.get(id=id)
				tempMessage.deleted = True
				tempMessage.save()

	if request.user.is_anonymous():
		return redirect('root_index')
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
	return render(request, 'protoChat/inbox.html', context)

def postRequest(request):
	if request.method == "POST":
		for key in request.POST:
			if key[:5] == 'check':
				id = key[5:]
				tempMessage = models.Message.objects.get(id=id)
				tempMessage.deleted = True
				tempMessage.save()

def index(request):
    """Chat API index page."""
    postRequest(request)
    return HttpResponse("Testing")

def getRequest(request):
	if request.user.is_anonymous():
		return redirect('root_index')
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
		return redirect('root_index')
	else:
		user = ProfileInfo.objects.get(user = request.user)
	message_id = request.args['id']
	
	message = models.Message.objects.filter(recipient=user).filter(id=message_id)
	message.deleted = True
	message.save()
	
















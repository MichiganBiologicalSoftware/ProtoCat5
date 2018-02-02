"""Define the basic views for users."""
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from User.models import *

def index(request):
    """User index page."""
    return HttpResponse("Testing")
# Login

def login_user(request):
	current_profile_info = request.user
	if (not current_profile_info.is_anonymous()):
		current_profile_info = UserInfo.objects.get(user = current_profile_info)
	else:
		current_profile_info = None
	context = {
		'title': 'ProtoCat - Login',
		'current_profile_info': current_profile_info,
	}
	return render(request, 'login.html', context)

def submit_login(request):
	try:
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username = username, password = password)

		if user is not None:
			# the pasword verified for the user
			if user.is_active:
				login(request, user)
				profile_info = UserInfo.objects.get(user = user)
				return JsonResponse({'success': True, 'location': '/'})
			else:
				return JsonResponse({'success': False})
		else:
			return JsonResponse({'success': False, 'error': 'Incorrect username/password combination'})
	except:
		return JsonResponse({'success': False, 'error': 'Please enter both the username and password'})


# Sign up

def sign_up(request):
	current_profile_info = request.user
	if (not current_profile_info.is_anonymous()):
		current_profile_info = UserInfo.objects.get(user = current_profile_info)
	else:
		current_profile_info = None
	context = {
		'title': 'ProtoCat - Sign Up',
		'current_profile_info': current_profile_info,
	}
	return render(request, 'sign_up.html', context)


def submit_sign_up(request):
	current_profile_info = request.user
	if (not current_profile_info.is_anonymous()):
		current_profile_info = UserInfo.objects.get(user = current_profile_info)
	else:
		current_profile_info = None
	try:
		# grab data to verify user
		username = request.POST['username']
		password = request.POST['password']
		email = request.POST['email']
		print(username)
		user = User.objects.create_user(username, email, password)
		# user = authenticate(username = username, password = password)
		profile_info = UserInfo(user = user)
		profile_info.save()
		current_profile_info = profile_info
		login(request, user)
		return JsonResponse({'success': True, 'location': '/'})
	except Exception as inst:
		print(inst)
		return JsonResponse({'success': False})

# Log Off
def logoff(request):
	logout(request)
	return HttpResponseRedirect('/')

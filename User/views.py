"""Define the basic views for users."""
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.views import logout
from django.contrib.auth.models import User
from User.models import *
from User.send_email import send_verification_email

def index(request):
	"""User index page."""
	# Redirects to user_id if logged in, to login page if not
	current_profile_info = request.user
	if current_profile_info.is_authenticated():
		current_profile_info = UserInfo.objects.get(user = current_profile_info)
	else:
		current_profile_info = None
	if current_profile_info is not None:
		return redirect('/user/' + str(request.user.id))
	return redirect('/user/login')

def user(request, user_id):
	"""User index page."""
	current_profile_info = request.user
	if (not current_profile_info.is_anonymous()):
		current_profile_info = UserInfo.objects.get(user = current_profile_info)
	else:
		current_profile_info = None

	user = UserInfo.objects.get(id = user_id)
	#user_created_protocols = Protocol.objects.filter(author = user).order_by('-upload_date')
	#user_created_notes = ProtocolComment.objects.filter(author = user).order_by('-upload_date')
	#user_rated_protocols = ProtocolRating.objects.filter(person = user).order_by('-score')

	title = 'ProtoCat - ' + str(user.user)

	context = {
		'title': title,
		'current_profile_info': current_profile_info,
		'profile_info': user,
		# 'user_created_protocols': user_created_protocols,
		# 'user_rated_protocols': user_rated_protocols,
		# 'notes': user_created_notes
	}

	# either allow user to edit or not
	if (current_profile_info != user):
		return render(request, 'user.html', context)
	else:
		return render(request, 'edit_user.html', context)

# Login

def login_user(request):
	current_profile_info = request.user
	if current_profile_info.is_authenticated():
		current_profile_info = UserInfo.objects.get(user = current_profile_info)
	else:
		current_profile_info = None
	context = {
		'title': 'ProtoCat - Login',
		'current_profile_info': current_profile_info,
	}
	if current_profile_info is not None:
		return redirect('/user/')
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
		if not username or not password or not email:
			return JsonResponse({'success': False, 'location': '/user/signup'})
		user = User.objects.create_user(username, email, password)
		# user = authenticate(username = username, password = password)
		profile_info = UserInfo(user = user)
		profile_info.save()
		current_profile_info = profile_info
		login(request, user)
		send_verification_email(user)
		return JsonResponse({'success': True, 'location': '/'})
	except Exception as inst:
		print(inst)
		return JsonResponse({'success': False})

# Log Off
def logoff(request):
	logout(request)
	return HttpResponseRedirect('/')

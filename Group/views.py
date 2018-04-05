"""Define the basic views for groups."""

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    """Group index page."""
    return HttpResponse("Testing")

def group_create(request):
	#create a new organization
	return HttpResponseRedirect('/')

def group_signup(request):
	if request.method == 'GET':
		current_profile_info = request.user
		if (not current_profile_info.is_anonymous()):
			current_profile_info = ProfileInfo.objects.get(user = current_profile_info)
		else:
			current_profile_info = None
		return render(request, 'GroupSignUp.html')
	elif request.method == 'POST':
		return render(request, 'GroupSignUp.html')

def add_group_protocol(request):
	current_profile_info = request.user
	if (not current_profile_info.is_anonymous()):
		current_profile_info = ProfileInfo.objects.get(user = current_profile_info)
	else:
		current_profile_info = None
	try:
		org_id = request.POST['group_id']
		pro_id = request.POST['protocol_id']
		org = Group.objects.get(id = org_id)
		pro = Protocol.objects.get(id=pro_id)
		if Group_Protocol.objects.filter(protocol = pro, group = org).count()==0:
			org_pro = Group_Protocol(protocol = pro, group = org)
			org_pro.save()
		else:
			print("Already exist")
		return protocol_by_group(request, org_id) #THIS LINE WILL NEED TO CHANGE, ALI SAID FUNCTION WON'T EXIST
	except:
		print("error")
	return category_default(request)

def delete_group_protocol(request):
	current_profile_info = request.user
	if (not current_profile_info.is_anonymous()):
		current_profile_info = ProfileInfo.objects.get(user = current_profile_info)
	else:
		current_profile_info = None

	try:
		org_id = request.POST['group_id']
		pro_id = request.POST['protocol_id']
		org = Group.objects.get(id = org_id)
		pro = Protocol.objects.get(id=pro_id)
		if Group_Protocol.objects.filter(protocol = pro, group = org)==None:
			print("Entry does not exist")
		else:
			Group_Protocol.objects.filter(protocol = pro, group = org).delete()
		return protocol_by_group(request, org_id) #THIS LINE WILL NEED TO CHANGE, ALI SAID FUNCTION WON'T EXIST
	except:
		print("error")
		return category_default(request)

def protocol_by_group(request, group_id):
	current_profile_info = request.user
	if (not current_profile_info.is_anonymous()):
		current_profile_info = ProfileInfo.objects.get(user = current_profile_info)
	else:
		current_profile_info = None
	org = Group.objects.get(id = group_id)
	protocols = Group_Protocol.objects.filter(group = org)
	isAdmin = None
	try:
		if Membership.objects.get(user = current_profile_info, group = org).isAdmin:
			isAdmin = True
	except:
		print("no valid user or group")
	result_pro = []
	for protocol in protocols:
		result_pro.append(Protocol.objects.get(id = protocol.protocol.id))
	text = 'ProtoCat'
	context = {
		'title': 'ProtoCat - Browse Categories by Group',
		'parent_category': None,
		'categories': None,
		'protocols': result_pro,
		'current_profile_info': current_profile_info,
		'isAdmin': isAdmin,
		'org': org,
	}
	return render(request, 'protocol_by_group.html', context)
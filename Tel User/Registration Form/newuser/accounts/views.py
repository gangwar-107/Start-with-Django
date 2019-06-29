from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth

# Create your views here.
from django.http import HttpResponse

def homeView(request):
	return render(request,'index.html')

def register(request):
	if request.method == 'POST':
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		username = request.POST['username']
		password = request.POST['password1']
		email = request.POST['email']

		user = User.objects.create_user(username = username,email= email,password = password,first_name=first_name,last_name=last_name)

		user.save()
		return redirect('/')
	else:
		return render(request,'index.html')

# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.views import generic
from django.contrib.auth.decorators import login_required
from construction.forms import ContactForm
from construction.models import Nation,Contact

# Create your views here.
@login_required
def home(request):
	return render(request,'templates/homepage.html')

@login_required
def about(request):
	return render(request,'templates/about.html')
	
@login_required
def services(request):
	return render(request,'templates/services.html')
	
@login_required
def contacts(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('success')
	else:
		form = ContactForm()
	return render(request,'templates/contacts.html',{'form': form})
	
def success(request):
	return render(request,'templates/success.html')

def new(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('success')
	else:
		form = ContactForm()
	return render(request,'templates/new.html',{'form': form})

def signup(request):
		if request.method == 'POST':
			form = UserCreationForm(request.POST)
			if form.is_valid():
				form.save()
				messages.success(request, 'Account created successfully')
				username = form.cleaned_data.get('username')
				raw_password = form.cleaned_data.get('password1')
				user=User.objects.create_user(username,raw_password)
				user.save()
				user = authenticate(username=username, password=raw_password)
				login(request, user)
				return redirect('home')
		else:
			form = UserCreationForm()
		return render(request, 'registration/signup.html', {'form': form})

class CountryList(generic.ListView):
	model=Nation
	context_object_name='Countries'
	template_name='templates/country.html'

	def get_queryset(self):
		return Nation.objects.all().order_by('id')

class CountryDetail(generic.DetailView):
	model=Nation
	context_object_name='Countries'
	template_name='templates/CountryDetail.html'

class CountryDelete(generic.DeleteView):
	model=Nation
	context_object_name = 'Countries'
	success_url ='success'
	template_name ='Delete.html'
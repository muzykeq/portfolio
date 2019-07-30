from django.shortcuts import render

# Create your views here.

def TodolistHome(request):
	return render(request, 'todo/todolist-home.html')
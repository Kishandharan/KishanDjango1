from django.shortcuts import render
import os

def home(request):
	dir1 = "C:/Coding/Python/pplpip" #This path can be changed
	os.chdir(dir1)
	list1 = os.listdir()
	return render(request, 'app1/index.html', {'param1':list1, 'param2':dir1})

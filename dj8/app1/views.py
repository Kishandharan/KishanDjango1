from django.shortcuts import render
from app1.forms import inputweb

def home(request):
	if request.method == "POST":
		form1=inputweb(request.POST)
		if form1.is_valid():
			data = form1.cleaned_data
			num1 = data.get("num1")
			fact1 = factorial(num1)
			return render(request, 'app1/index.html', {'param1':fact1, 'form':form1})
	else:
		form1=inputweb()
	return render(request, 'app1/index.html', {'form':form1})

def factorial(num1):
	result=1
	for i in range(1, num1+1, 1):
		result=result*i
	return result
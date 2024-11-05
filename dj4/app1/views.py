from django.shortcuts import render
from app1.forms import inputweb
def home(request):
	if request.method == "POST":
		form1=inputweb(request.POST)
		if form1.is_valid():
			form1.save()
			return render(request, "app1/index.html", {"form":form1, "msg1":"Success!"})
	else:
		form1=inputweb()
	return render(request, "app1/index.html", {"form":form1})

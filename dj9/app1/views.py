from django.shortcuts import render

def home(request):
    out=eval(input("math>"))
    return render(request, 'app1/index.html', {'param1':out})

from django.shortcuts import render

def home(request):
    num1 = 5
    squ1 = square(num1)
    return render(request, 'app1/index.html', {'param1': squ1})

def square(num1):
    return num1*num1
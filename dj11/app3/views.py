from django.shortcuts import render

def home(request):
    num1 = 5
    fact1 = fact(num1)
    square1 = square(num1)

    return render(request, "app3/index.html", {"param1": fact1, "param2": square1})

def square(num1):
    return num1*num1

def fact(num1):
    result=num1
    for i in range(result-1, 0, -1):
        result = result * i 
    return result
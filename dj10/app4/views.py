from django.shortcuts import render

def home(request):
    num1 = 5
    fact1 = fact(num1)
    square1 = square(num1)

    return render(request, 'app4/index.html', {'param1': square1, 'param2': fact1, 'param3': num1})

def fact(num1):
    result = num1
    for i in range(num1-1, 1, -1):
        result = result * i
    return result

def square(num1):
    return num1*num1
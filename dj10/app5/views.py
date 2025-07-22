from django.shortcuts import render

def home(request):
    list1 = [] 
    list2 = []

    for x in range(1, 10):
        list1.append(fact(x))
        list2.append(square(x))

    return render(request, 'app5/index.html', {'param1': list1, 'param2': list2})

def fact(num1):
    result = num1
    for i in range(num1-1, 1, -1):
        result = result * i
    return result

def square(num1):
    return num1*num1
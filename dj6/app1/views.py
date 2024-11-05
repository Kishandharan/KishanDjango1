from django.shortcuts import render
import os

def home(request):
	os.chdir('C:/Coding/Django/')
	fname = 'olympics.csv'
	li1 = oly1(fname)
	li2 = []
	part1=li1[0]
	part2=li1[1]
	print(part2)
	for x in part2:
		a = r"{% static "
		b = " %}"
		info1 = a+"'AUS.png'"+b
		li2.append(info1)
		print(info1)
	return render(request, 'app1/index.html', {'param1':part1, 'param2':part2, 'param3':li2})

def oly1(fname):
    f1 = open(fname, 'r')
    li1 = []
    flags = []
    for x in range(10):
        s1 = f1.readline().replace('\n','')
        li2 = s1.split(',')
        flags.append(li2[0]+".png")
        li1.append(li2)
    return(li1,flags)


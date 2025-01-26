from django.shortcuts import render
import random
import string
from django.http import HttpResponse


def home(request):
    return render(request, 'base.html')

def task_1(request):
    name =  request.GET.get('name', 'Aktan')
    return render(request, 'blog/task_1.html', {'name': name})

def task_2(request):
    first = int(request.GET.get('a',5))
    second = int(request.GET.get('b',10))
    res = (f'{first} + {second} = {first + second}')
    return render(request,'blog/task_2.html', {'first': first,'second': second ,'res': res})

def task_3(request):
    number = int(request.GET.get('num',7))
    checking = [{number},"Jup" if number % 2 == 0 else "Tak"]
    return render(request, 'blog/task_3.html', {'number': number, 'checking': checking })

def task_4(request):
    text = request.GET.get('text', 'Python Django Api Java Backend')
    n = int(request.GET.get('n',5))
    words = text.split()
    filtered_words = [word for word in words if len(word) > n]
    return render(request, 'blog/task_4.html', {'filtered_words': filtered_words})

def task_6(request):
    age = int(request.GET.get('age', 2007))
    res = (2025 - age)
    return render(request, 'blog/task_6.html', {'age':age, 'res': res})


def task_7(request):
    number = int(request.GET.get('n', 5 ))
    context = [f'{number} x {i} = {number * i }' for i in range(1,11)]
    return render(request, 'blog/task_7.html',{'number': number, 'context': context})

def task_8(request):
    numbers = request.GET.get('numbers', '').split(',')
    numbers_list = list(map(int, numbers))
    max_number = max(numbers_list)
    return render(request, 'blog/task_8.html', {'max_number':max_number})

def task_9(request):
    celsius = request.GET.get('celsius', 30)
    fahrenheit = (float(celsius) * 9 / 5) + 32
    return render(request, 'blog/task_9.html', {'fahrenheit' :fahrenheit})

def task_10(request):
    length = int(request.GET.get('length', 8))
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return render(request, 'blog/task_10.html', {'password':password})
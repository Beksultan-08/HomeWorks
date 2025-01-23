from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<p>Hello, world. You`re at the polls index.</p>")

def factorial(request):
    number = int(request.GET.get['number',10])
    result = 1
    for i in range(1, number + 1):
        result *= i
    return HttpResponse(f"<h1>Result: {result}</h1>")

def info(request):
    print(request.GET)
    return HttpResponse(
        f'<h1>Info</h1><br>'
        f'<p>{request.build_absolute_uri()}</p>'
        f'<p>{request.method}</p>'
        f'<p>Name:{request.GET["name"]}<br>Age:{request.GET["age"]}</p>'
    )

def hello(request):
    name = request.GET.get('name')
    return HttpResponse(f'Hello {name}')

def sum(request):
    a = request.GET.get('a')
    b = request.GET.get('b')
    res = int(a) + int(b)
    return HttpResponse(f'Result: {res}')

def check(request):
    number = request.GET.get('number')
    a = ["Tak san" if int(number) % 2 == 1 else "Jup san"]
    return HttpResponse(F"{number} - {a}")

def filter(request):
    text = request.GET.get('text')
    n = int(request.GET.get('n'))
    s = text.split()
    d = [i for i in s if len(i) > n]
    return HttpResponse(" ".join(d))
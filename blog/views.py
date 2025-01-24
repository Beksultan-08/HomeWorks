from django.shortcuts import render
from django.http import HttpResponse


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

def task_1(request):
    name =  request.GET.get('name', 'Aktan')
    return render(request, 'blog/task_1.html', {'name': name})

def task_7(request):
    number = int(request.GET.get('n', 5 ))
    context = [f'{number} x {i} = {number * i }' for i in range(1,11)]
    return render(request, 'blog/task_7.html',{'number': number, 'context': context})

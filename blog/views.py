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

def palindrome(request):
    word = request.GET.get('word')
    if word[0].lower == word[-1].lower:
        return HttpResponse(f'{word} - palindrome')

def age(request):
    year = request.GET.get('year')
    return HttpResponse(f'Your age - {2025 - int(year)}')

def multiplication(request):
    n = int(request.GET.get('n'))
    return HttpResponse(
        f"<p>{n } * { 1 } = {n * 1}<p/>"
        f"<p>{n } * { 2 } = {n * 2}<p/>"
        f"<p>{n } * { 3 } = {n * 3}<p/>"
        f"<p>{n } * { 4 } = {n * 4}<p/>"
        f"<p>{n } * { 5 } = {n * 5}<p/>"
        f"<p>{n } * { 6 } = {n * 6}<p/>"
        f"<p>{n } * { 7 } = {n * 7}<p/>"
        f"<p>{n } * { 8 } = {n * 8}<p/>"
        f"<p>{n } * { 9 } = {n * 9}<p/>"
        f"<p>{n } * { 10 } = {n * 10}<p/>"
    )

def max(request):
    numbers = request.GET.get('numbers')
    a = max(numbers)
    return HttpResponse(a)

def temp(request):
    celsius = request.GET.get('celsius')
    fahrenheit = (celsius * 9/5) + 32
    return HttpResponse(F"{celsius} = {fahrenheit}")
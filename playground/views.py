from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def say_hello(request):
    return HttpResponse("Hello World")

def say_hello_html(request):
    return render(request, "playground/hello.html", {'name':'지인아', 'greeting':'안뇽~'})

def say_bye_html(request):
    context = {
        'singer' : 'Adel',
        'title' : 'All I Ask'
    }
    return render(request, "playground/bye.html", context=context)
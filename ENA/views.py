from django.shortcuts import render

def show_ena(request):
    return render(request, "ENA/ena.html")

def show_moony(request):
    return render(request, "ENA/moony.html")

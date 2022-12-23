from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'rental/home/index.html')


def rent(request):
    return render(request, 'rental/rent/rent.html')


def contact(request):
    return render(request, 'rental/contact/contact.html')


def about(request):
    return render(request, 'rental/about/about.html')

from django.contrib import messages
from django.core import mail
from django.contrib.auth import authenticate, update_session_auth_hash
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import SearchBarFilter, Register, CarReservation
from .models import Car, Rental
from .utils import searchCars


def index(request):
    return render(request, 'rental/home/index.html')


def rent(request):
    cars = Car.objects.all()
    if request.method == 'GET':
        searchFilter = SearchBarFilter(request.GET)
        if searchFilter.is_valid():
            cars = searchCars(searchFilter)
            return render(request, 'rental/rent/rent.html', {'form': searchFilter, 'cars': cars})
        else:
            searchFilter = SearchBarFilter()
            return render(request, 'rental/rent/rent.html', {'form': searchFilter, 'cars': cars})


def rentCar(request, car_id):
    car = Car.objects.get(id=car_id)
    return render(request, 'rental/rent/rentCar.html', {'car': car})


@login_required()
def carReservation(request, car_id):
    car = Car.objects.get(id=car_id)
    if request.method == 'POST':
        form = CarReservation(request.POST)
        if form.is_valid():
            form.save(car_id, request.user)
            return redirect('rental:rental')
    form = CarReservation()
    return render(request, 'rental/rent/carReservation.html', {'car': car, 'form': form})


def contact(request):
    return render(request, 'rental/contact/contact.html')


def about(request):
    return render(request, 'rental/about/about.html')


def register(request):
    if request.method == "POST":
        form = Register(request.POST)
        if form.is_valid():
            user = form.save()
            with mail.get_connection() as connection:
                mail.EmailMessage(
                    'Welcome to Car Rental',
                    'Thank you for registering to our site',
                    'car2go@mail.com', [user.email],
                    connection=connection,
                ).send()
            login(request)
            messages.success(request, "Registration successful.")
            return redirect("rental:homepage")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = Register()
    return render(request, 'rental/register/register.html', context={"register_form": form})


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('rental:homepage')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request, 'rental/login/login.html', context={"login_form": form})


@login_required
def logout(request):
    storage = messages.get_messages(request)
    for message in storage:
        pass
    for _ in list(storage._loaded_messages):
        del storage._loaded_messages[0]
    django_logout(request)
    return HttpResponseRedirect('/home')


@login_required
def profile(request):
    user = request.user
    return render(request, 'rental/profile/profile.html', context={'user': user})


@login_required
def reservations(request):
    user = request.user
    reservations = Rental.objects.filter(user=user)
    return render(request, 'rental/profile/reservations.html', context={'reservations': reservations})


@login_required
def editProfile(request):
    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Password changed successfully.")
            return redirect("rental:profile")
        else:
            messages.error(request, "Invalid password.")
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'rental/profile/editProfile.html', context={"form": form})

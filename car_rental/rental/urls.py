from django.urls import path

from . import views

app_name = 'rental'

urlpatterns = [
    path('', views.index, name='homepage'),
    path('rent/', views.rent, name='rental'),
    path('rent/<int:car_id>/', views.rentCar, name='rentalCar'),
    path('rent/<int:car_id>/reservation', views.carReservation, name='reservation'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/reservations/', views.reservations, name='reservations'),
    path('profile/edit/', views.editProfile, name='editProfile'),
]
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('rent/', views.rent, name='rental'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
]
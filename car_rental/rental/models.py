from django.db import models


class CarType(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Car(models.Model):
    name = models.CharField(max_length=100)
    type = models.ForeignKey(CarType, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='car_images')


class Rental(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.car.name

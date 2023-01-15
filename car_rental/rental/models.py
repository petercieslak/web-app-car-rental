from django.db import models


class CarType(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class PetrolType(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Car(models.Model):
    name = models.CharField(max_length=100)
    type = models.ForeignKey(CarType, on_delete=models.CASCADE)
    petrol = models.ForeignKey(PetrolType, on_delete=models.CASCADE)
    price = models.IntegerField()
    seats = models.IntegerField()
    image = models.ImageField(upload_to='rental/static/rental/car_images')


class Rental(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    startDate = models.DateField()
    endDate = models.DateField()
    phoneNumber = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, blank=True)

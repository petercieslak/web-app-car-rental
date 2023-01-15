from django import forms
from django.contrib.auth import forms as auth_forms
from django.contrib.auth.models import User
from django.forms import SelectDateWidget

from .models import CarType, PetrolType, Car, Rental

CAR_TYPES = list(CarType.objects.all().values_list('name', 'name'))
CAR_TYPES = [('Any', 'Any')] + CAR_TYPES
PETROL_TYPES = list(PetrolType.objects.all().values_list('name', 'name'))
PETROL_TYPES = [('Any', 'Any')] + PETROL_TYPES


class SearchBarFilter(forms.Form):
    type = forms.CharField(label='Car type', widget=forms.Select(choices=CAR_TYPES, attrs={'id': 'car_type'}),
                           initial='Any')

    min_price = forms.IntegerField(label='Min price', widget=forms.NumberInput(attrs={'id': 'min_price'}),
                                   initial=0, required=False)

    max_price = forms.IntegerField(label='Max price', widget=forms.NumberInput(attrs={'id': 'max_price'}),
                                   initial=Car.objects.order_by('-price')[0].price, required=False)

    petrol = forms.CharField(label='Petrol type', widget=forms.Select(choices=PETROL_TYPES,
                                                                      attrs={'id': 'petrol_type'}))


class Register(auth_forms.UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(Register, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class CarReservation(forms.Form):
    name = forms.CharField(label='Name', widget=forms.TextInput(attrs={'id': 'name'}),
                           error_messages={'required': 'Please enter your name'},
                           )
    surname = forms.CharField(label='Surname', widget=forms.TextInput(attrs={'id': 'surname'}),
                              error_messages={'required': 'Please enter your surname'})
    phone = forms.CharField(label='Phone number', widget=forms.TextInput(attrs={'id': 'phone'}),
                            error_messages={'required': 'Please enter your phone number'})
    start_date = forms.DateField(widget=SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day")))
    end_date = forms.DateField(widget=SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day")))

    def save(self, car_id, user):
        car = Car.objects.get(id=car_id)
        rent = Rental.objects.create(car=car, name=self.cleaned_data['name'], surname=self.cleaned_data['surname'],
                                     startDate=self.cleaned_data['start_date'], endDate=self.cleaned_data['end_date'],
                                     phoneNumber=self.cleaned_data['phone'], user=user)
        rent.save()



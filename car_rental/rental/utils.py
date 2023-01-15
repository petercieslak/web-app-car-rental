from .models import Car


def searchCars(searchFilter):
    if searchFilter.data.get('type') == 'Any' and searchFilter.data.get('petrol') != 'Any':
        cars = Car.objects.filter(price__gte=searchFilter.data.get('min_price'),
                                  price__lte=searchFilter.data.get('max_price'),
                                  petrol__name=searchFilter.data.get('petrol'))
    elif searchFilter.data.get('petrol') == 'Any' and searchFilter.data.get('type') != 'Any':
        cars = Car.objects.filter(type__name=searchFilter.data.get('type'),
                                  price__gte=searchFilter.data.get('min_price'),
                                  price__lte=searchFilter.data.get('max_price'))
    elif searchFilter.data.get('type') == 'Any' and searchFilter.data.get('petrol') == 'Any':
        cars = Car.objects.filter(price__gte=searchFilter.data.get('min_price'),
                                  price__lte=searchFilter.data.get('max_price'))
    else:
        cars = Car.objects.filter(type__name=searchFilter.data.get('type'),
                                  petrol__name=searchFilter.data.get('petrol'),
                                  price__gte=searchFilter.data.get('min_price'),
                                  price__lte=searchFilter.data.get('max_price'))
    return cars

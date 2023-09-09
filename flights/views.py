from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from flights.models import Airport, Flight, Passenger
from django import forms
from django.urls import reverse

# Create your views here.

def index(request):
    if request.user.is_authenticated:
        return render(request, 'flights/index.html', {
            'flights':Flight.objects.all().order_by('id')
        })
    else:
        return HttpResponseRedirect(reverse("users:login"))

def flight(request, flight_id):
    if request.user.is_authenticated:
        if flight_id <= Flight.objects.count():
            flight = Flight.objects.get(id=flight_id)
            passengers = flight.passenger.all()
            return render(request, 'flights/flight.html',{
                'flight': flight,
                'flight_id':flight_id,
                'passengers':passengers,
                'non_passengers': Passenger.objects.exclude(flights=flight).all()
            })

        else:
            return HttpResponseRedirect(reverse("flights:index"))
    else:
        return HttpResponseRedirect(reverse("users:login"))

def book(request, flight_id):
    if request.user.is_authenticated:
        if request.method == "POST":
            flight = Flight.objects.get(id=flight_id)
            passenger = Passenger.objects.get(id=int(request.POST["passenger"]))
            passenger.flights.add(flight)
            return HttpResponseRedirect(reverse('flights:flight', args=(flight.id,)))
    else:
        return HttpResponseRedirect(reverse("users:login"))

class FlightLookUp(forms.Form):
    flight_count = Flight.objects.count()
    flight_id = forms.IntegerField(max_value=flight_count,min_value=1)
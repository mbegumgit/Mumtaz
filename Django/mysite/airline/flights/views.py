from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Flight, Airport, Passenger
from django.urls import reverse

# Create your views here.
def indexf(request):
    #return HttpResponse("Flights")
    content = Flight.objects.all()
    return render(request, "flights/indexf.html", {'flights': content})

def flight(request, flight_id):
    #return HttpResponse("Flights")
    try:
        flight = Flight.objects.get(id=flight_id)
    
    except Flight.DoesNotExist:
        raise Http404("Flight does not exist")
    content = {"flight": flight,
               "passengers": flight.passengers.all(),
               "non_passengers": Passenger.objects.exclude(flights=flight).all()
                } 
    return render(request, "flights/flight.html", content)
def book(request, flight_id):
      try:
          passenger_id = int(request.POST["passenger"])
          flight = Flight.objects.get(pk=flight_id)
          passenger = Passenger.objects.get(pk=passenger_id)
      except KeyError:
          return render(request, "flights/error.html", {"message": "No selection."})
      except Flight.DoesNotExist:
          return render(request, "flights/error.html", {"message": "No flight."})
      except Passenger.DoesNotExist:
          return render(request, "flights/error.html", {"message": "No passenger."})
      passenger.flights.add(flight)
      return HttpResponseRedirect(reverse("flight", args=(flight_id,))) 
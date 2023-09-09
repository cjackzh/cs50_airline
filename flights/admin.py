from django.contrib import admin
from flights.models import Airport, Flight, Passenger

# Register your models here.
admin.site.register(Airport)
admin.site.register(Passenger)


class FlightAdmin(admin.ModelAdmin):
    list_display = ('id', 'origin', 'destination', 'duration')

admin.site.register(Flight, FlightAdmin)
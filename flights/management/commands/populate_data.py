from django.core.management.base import BaseCommand
from flights.models import Flight, Airport

class Command(BaseCommand):
    help="Populate data in Flight model"

    def handle(self,*args,**kwargs):
        airports = Airport.objects.all().order_by('id')
        
        data_to_add = [
            {"origin":airports[0],"destination":airports[1],"duration":450},
            {"origin":airports[2],"destination":airports[3],"duration":300},
            {"origin":airports[3],"destination":airports[0],"duration":500},
            {"origin":airports[2],"destination":airports[0],"duration":475}
        ]

        # data_to_add = [
        #     {'code':'JFK','city':'New York'},
        #     {'code':'LHR','city':'London'},
        #     {'code':'CDG','city':'Paris'},
        #     {'code':'NRT','city':'Tokyo'}
        # ]
        count = len(data_to_add)

        for data in data_to_add:
            # Airport.objects.create(
            #     code = data["code"],
            #     city = data['city']
            # )
            flight = Flight(**data)
            flight.save()

        self.stdout.write(self.style.SUCCESS(f'Successfully added {count} records to Flight model.'))
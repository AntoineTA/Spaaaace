import factory
from random import randint, choice, random
from datetime import datetime

from .models import *

class OperatorFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('sentence', nb_words=1)
    country = factory.Faker('sentence', nb_words=1)

    class Meta:
        model = Operator

class SatelliteFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('sentence', nb_words=1)
    country_un_registery = choice(['USA', 'France', ''])
    usage1 = choice(['Civil', 'Commercial', 'Government', 'Military'])
    usage2 = choice(['Civil', 'Commercial', 'Government', 'Military', ''])
    purpose1 = choice(['Communications', 'Space exploration', 'Technology Demostration', ''])
    purpose2 = choice(['Communications', 'Space exploration', 'Technology Demostration', ''])
    orbit_class = choice(['LEO', 'MEO', 'GEO', 'ELL'])
    perigee_km = randint(100, 1000000)
    apogee_km = randint(100, 1000000)
    inclination_deg = random()*10000
    period_minutes = random()*10000
    launch_mass_kg = randint(1, 10000)
    launch_date = datetime.now()
    expected_lifetime_yrs = random()*100
    launch_site = factory.Faker('sentence', nb_words=1)
    launch_vehicle = factory.Faker('sentence', nb_words=1)
    operator = factory.SubFactory(OperatorFactory)

    class Meta:
        model = Satellite

import os, sys, csv
import django
from datetime import datetime

# DISABLE_COLLECTSTATIC = 1

# BASE_DIR = Path(__file__).resolve().parent

# setup script
# settingsPath = os.path.join(BASE_DIR, "Spaaaace.settings")
# print(settingsPath)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Spaaaace.settings')
django.setup()

from earthsat.models import *

# data_file = os.path.join(BASE_DIR, "satellites.csv")
data_file = 'satellites.csv'

# delete all existing data before importing
Satellite.objects.all().delete()
Operator.objects.all().delete()

# Get data from file
satellites = []
operators = set()

with open(data_file) as csv_file:
    reader = csv.reader(csv_file, delimiter=';')

    # skip header row
    header = reader.__next__()

    for l in reader:
        satellite = {}

        usage1, usage2 = '', ''
        usages = l[2].split('/')
        if len(usages) == 1:
            usage1 = usages[0]
        if len(usages) == 2:
            usage1, usage2 = usages

        purpose1, purpose2 = '', ''
        purposes = l[3].split('/')
        if len(purposes) == 1:
            purpose1 = purposes[0]
        if len(purposes) == 2:
            purpose1, purpose2 = purposes

        satellite = {
            'name': l[0],
            'country_un_registery': l[1],
            'usage1': usage1,
            'usage2': usage2,
            'purpose1': purpose1,
            'purpose2': purpose2,
            'orbit_class': l[4],
            'perigee_km': int(l[5]) if l[5] != '' else None,
            'apogee_km': int(l[6]) if l[6] != '' else None,
            'inclination_deg': float(l[7]) if l[7] != '' else None,
            'period_minutes': float(l[8]) if l[8] != '' else None,
            'launch_mass_kg': int(l[9]) if l[9] != '' else None,
            'launch_date': datetime.strptime(l[10], '%d.%m.%Y'),
            'expected_lifetime_yrs': float(l[11]) if l[11] != '' else None,
            'launch_site': l[12],
            'launch_vehicle': l[13],
            'operator_name': l[14]
        }

        satellites.append(satellite)
        operators.add((l[14], l[15]))

    print('Loaded {} items to memory'.format(len(satellites)))

    # Insert data into database
    print('Adding operators to database...')
    count = 0
    operator_row = {}
    for name, country in operators:
        row = Operator.objects.create(
            name=name,
            country=country
        )
        row.save()

        # keep track of row for foreign key
        operator_row[name] = row

        count += 1
        if (count % 100) == 0:
            print('{}/{}'.format(count, len(operators)))

    print('Finished.')


    print('Adding satellites to database...')
    count = 0
    for s in satellites:
        row = Satellite.objects.create(
            name = s['name'],
            country_un_registery = s['country_un_registery'],
            usage1 = s['usage1'],
            usage2 = s['usage2'],
            purpose1 = s['purpose1'],
            purpose2 = s['purpose2'],
            orbit_class = s['orbit_class'],
            perigee_km = s['perigee_km'],
            apogee_km = s['apogee_km'],
            inclination_deg = s['inclination_deg'],
            period_minutes = s['period_minutes'],
            launch_mass_kg = s['launch_mass_kg'],
            launch_date = s['launch_date'],
            expected_lifetime_yrs = s['expected_lifetime_yrs'],
            launch_site = s['launch_site'],
            launch_vehicle = s['launch_vehicle'],
            # when a row is passed, Django will automatically create a foreign key
            operator=operator_row[s['operator_name']]
        )
        row.save()

        count += 1
        if (count % 100) == 0:
            print('{}/{}'.format(count, len(satellites)))

    print('Finished.')






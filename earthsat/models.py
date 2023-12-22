from django.db import models

class Operator(models.Model):

    class Meta:
        ordering = ['name']
        
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)


class Satellite(models.Model):

    class Meta:
        ordering = ['name']

    USAGE_CHOICES = {
        'Civil': 'Civil',
        'Commercial': 'Commercial',
        'Government':'Government',
        'Military': 'Military'
    }

    ORBIT_CLASSES = {
    'LEO': 'Low Earth Orbit',
    'MEO': 'Medium Earth Orbit',
    'GEO': 'Geostationary',
    'ELL': 'Elliptical'
}

    name = models.CharField(max_length=255)
    country_un_registery=models.CharField(max_length=255, blank=True)
    usage1=models.CharField(max_length=255, choices=USAGE_CHOICES, blank=True)
    usage2=models.CharField(max_length=255, choices=USAGE_CHOICES, blank=True)
    purpose1=models.CharField(max_length=255, blank=True)
    purpose2=models.CharField(max_length=255, blank=True)
    orbit_class=models.CharField(max_length=255, choices=ORBIT_CLASSES, blank=True)
    perigee_km=models.IntegerField(null=True, blank=True)
    apogee_km=models.IntegerField(null=True, blank=True)
    inclination_deg=models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
    period_minutes=models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
    launch_mass_kg=models.IntegerField(null=True, blank=True)
    launch_date=models.DateField(blank=True, null=True)
    expected_lifetime_yrs=models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
    launch_site=models.CharField(max_length=255, blank=True)
    launch_vehicle=models.CharField(max_length=255, blank=True)
    operator=models.ForeignKey(Operator, on_delete=models.DO_NOTHING)

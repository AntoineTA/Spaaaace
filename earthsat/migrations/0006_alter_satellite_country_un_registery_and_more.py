# Generated by Django 5.0 on 2023-12-12 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('earthsat', '0005_alter_satellite_apogee_km_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='satellite',
            name='country_un_registery',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='satellite',
            name='launch_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='satellite',
            name='launch_site',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='satellite',
            name='launch_vehicle',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='satellite',
            name='orbit_class',
            field=models.CharField(blank=True, choices=[('LEO', 'Low Earth Orbit'), ('MEO', 'Medium Earth Orbit'), ('GEO', 'Geostationary'), ('ELL', 'Elliptical')], max_length=255),
        ),
        migrations.AlterField(
            model_name='satellite',
            name='purpose1',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='satellite',
            name='purpose2',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='satellite',
            name='usage1',
            field=models.CharField(blank=True, choices=[('Civil', 'Civil'), ('Commercial', 'Commercial'), ('Government', 'Government'), ('Military', 'Military')], max_length=255),
        ),
        migrations.AlterField(
            model_name='satellite',
            name='usage2',
            field=models.CharField(blank=True, choices=[('Civil', 'Civil'), ('Commercial', 'Commercial'), ('Government', 'Government'), ('Military', 'Military')], max_length=255),
        ),
    ]

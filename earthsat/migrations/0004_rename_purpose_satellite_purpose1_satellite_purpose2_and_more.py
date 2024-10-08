# Generated by Django 5.0 on 2023-12-12 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('earthsat', '0003_alter_satellite_expected_lifetime_yrs'),
    ]

    operations = [
        migrations.RenameField(
            model_name='satellite',
            old_name='purpose',
            new_name='purpose1',
        ),
        migrations.AddField(
            model_name='satellite',
            name='purpose2',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='satellite',
            name='usage1',
            field=models.CharField(choices=[('Civil', 'Civil'), ('Commercial', 'Commercial'), ('Government', 'Government'), ('Military', 'Military')], default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='satellite',
            name='usage2',
            field=models.CharField(choices=[('Civil', 'Civil'), ('Commercial', 'Commercial'), ('Government', 'Government'), ('Military', 'Military')], default='', max_length=255),
            preserve_default=False,
        ),
    ]

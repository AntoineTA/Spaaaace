from functools import reduce
import operator
from django.db.models import Q
from rest_framework import generics
from .models import *
from .serializers import *

class SatellitesList(generics.ListAPIView):
    queryset = Satellite.objects.all()
    serializer_class = SatelliteSerializer

class OperatorsList(generics.ListAPIView):
    queryset = Operator.objects.all()
    serializer_class = OperatorSerializer

class SatelliteDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Satellite.objects.all()
    serializer_class = SatelliteSerializer

class OperatorDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Operator.objects.all()
    serializer_class = OperatorSerializer

class SatelliteAdd(generics.CreateAPIView):
    serializer_class = SatelliteSerializer

class SatellitesQuery(generics.ListAPIView):
    def get_queryset(self):
        satellites = Satellite.objects.all()
        qp = self.request.query_params
        for key in qp.keys():
            # get list of values associated with the key
            values = qp.getlist(key) 

            # create a list of query, using Django Q Object
            queries = [Q(**{f'{key}': value}) for value in values]

            # link the queries with OR, then filter
            satellites = satellites.filter(reduce(operator.or_, queries))
        return satellites

    serializer_class = SatelliteSerializer




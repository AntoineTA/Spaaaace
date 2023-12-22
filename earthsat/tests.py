import json
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIRequestFactory, APITestCase

from .model_factories import *
from .serializers import *

class SatellitesListTest(APITestCase):
    good_url = ''

    def setUp(self):
        for i in range(300):
            SatelliteFactory.create(pk=i)
        self.good_url = reverse('satellites_list_api')

    def test_SatellitesListReturnSuccessful(self):
        response = self.client.get(self.good_url, format='json')
        response.render()
        self.assertEqual(response.status_code, 200)

    def test_SatellitesListPagination(self):
        response = self.client.get(self.good_url, format='json')
        data = json.loads(response.content)
        self.assertLessEqual(len(data), 100)

    def test_SatellitesListOrder(self):
        response = self.client.get(self.good_url, format='json')
        data = json.loads(response.content)
        names = []
        for r in data['results']:
            names.append(r['name'])
        self.assertEqual(names, sorted(names))

class OperatorsListTest(APITestCase):
    good_url = ''

    def setUp(self):
        for i in range(150):
            OperatorFactory.create(pk=i)
        self.good_url = reverse('operators_list_api')

    def test_OperatorsListReturnSuccessful(self):
        response = self.client.get(self.good_url, format='json')
        response.render()
        self.assertEqual(response.status_code, 200)

    def test_OperatorsListPagination(self):
        response = self.client.get(self.good_url, format='json')
        data = json.loads(response.content)
        self.assertLessEqual(len(data), 100)

    def test_OperatorsListOrder(self):
        response = self.client.get(self.good_url, format='json')
        data = json.loads(response.content)
        names = [d['name'] for d in data['results']]
        self.assertEqual(names, sorted(names))

class SatelliteDetailsTest(APITestCase):
    good_url = ''
    bad_url = ''
    update_url = ''
    delete_url = ''

    def setUp(self):
        for i in range(5):
            SatelliteFactory.create(pk=i)
        self.good_url = reverse('satellite_details_api', kwargs={'pk': 1})
        self.bad_url = 'api/satellite/H'
        self.update_url = reverse('satellite_details_api', kwargs={'pk': 2})
        self.delete_url = reverse('satellite_details_api', kwargs={'pk': 3})
    
    def test_SatelliteDetailsReturnSuccessful(self):
        response = self.client.get(self.good_url, format='json')
        response.render()
        self.assertEqual(response.status_code, 200)

    def test_SatelliteDetailsReturnOnBadPk(self):
        response = self.client.get(self.bad_url, format='json')
        self.assertEqual(response.status_code, 404)

    def test_SatelliteDetailsUpdate(self):
        response = self.client.patch(self.update_url, {'name': 'new_name'}, format='json')
        data = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['name'], 'new_name')

    def test_SatelliteDetailsDelete(self):
        response = self.client.delete(self.delete_url, format='json')
        self.assertEqual(response.status_code, 204)

class OperatorDetailsTest(APITestCase):
    good_url = ''
    bad_url = ''
    update_url = ''
    delete_url = ''

    def setUp(self):
        for i in range(5):
            OperatorFactory.create(pk=i)
        self.good_url = reverse('operator_details_api', kwargs={'pk': 1})
        self.bad_url = 'api/operator/H'
        self.update_url = reverse('operator_details_api', kwargs={'pk': 2})
        self.delete_url = reverse('operator_details_api', kwargs={'pk': 3})

    def test_OperatorDetailsReturnSucessful(self):
        response = self.client.get(self.good_url, format='json')
        response.render()
        self.assertEqual(response.status_code, 200)

    def test_OperatorDetailsReturnOnBadPk(self):
        response = self.client.get(self.bad_url, format='json')
        self.assertEqual(response.status_code, 404)

    def test_OperatorDetailsUpdate(self):
        response = self.client.patch(self.update_url, {'name': 'new_name', 'country': 'USA'}, format='json')
        data = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['name'], 'new_name')
        self.assertEqual(data['country'], 'USA')

    def test_OperatorDetailsDelete(self):
        response = self.client.delete(self.delete_url, format='json')
        self.assertEqual(response.status_code, 204)

class SatelliteAddTest(APITestCase):
    newSat = {}
    op = {}
    good_url = ''

    def setUp(self):
        self.op = OperatorFactory.create(pk=1)
        self.newSat = {"name": "Hello", "operator": {"id": self.op.id, "name": self.op.name, "country": self.op.country}}
        self.good_url = reverse('satellite_add_api')

    def test_SatelliteAddReturnSuccessful(self):
        response = self.client.post(self.good_url, self.newSat, format='json')
        self.assertEqual(response.status_code, 201)

    def test_SatelliteAddGetReturn(self):
        response = self.client.get(self.good_url, format='json')
        self.assertEqual(response.status_code, 405)

class SatellitesQueryTest(APITestCase):
    good_url = ''

    def setUp(self):
        for i in range(10):
            SatelliteFactory.create(pk=i)
        SatelliteFactory.create(pk=10, country_un_registery='CH', name='TestName')
        SatelliteFactory.create(pk=15, country_un_registery='CH')
        SatelliteFactory.create(pk=16, country_un_registery='UK')
        SatelliteFactory.create(pk=17, country_un_registery='CH')
        SatelliteFactory.create(pk=18, country_un_registery='UK')
        self.good_url = reverse('satellites_query_api')

    def test_SatellitesQueryReturnSucessful(self):
        response = self.client.get(self.good_url, format='json')
        response.render()
        self.assertEqual(response.status_code, 200)

    def test_SatelliteQuerySimpleQuery(self):
        query = '?country_un_registery=CH'
        response = self.client.get(self.good_url + query, format='json')
        data = json.loads(response.content)
        countries = {d['country_un_registery'] for d in data['results']}
        self.assertEqual(len(data['results']), 3)
        self.assertEqual(countries, {'CH'})

    def test_SatelliteQueryComplexQuery(self):
        query = '?country_un_registery=CH&name=TestName'
        response = self.client.get(self.good_url + query, format='json')
        data = json.loads(response.content)
        self.assertEqual(len(data['results']), 1)

    def test_SatelliteQueryMultiQuery(self):
        query = '?country_un_registery=CH&country_un_registery=UK'
        response = self.client.get(self.good_url + query, format='json')
        data = json.loads(response.content)
        countries = {d['country_un_registery'] for d in data['results']}
        self.assertEqual(len(data['results']), 5)
        self.assertEqual(countries, {'CH', 'UK'})




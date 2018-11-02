from rest_framework.test import APITestCase
from django.test import Client
from bicycle.models import Bicycle
from bicycle.serializers import BicycleSerializers


class BiclycleTests(APITestCase):

    c = Client()

    def test_can_get_biclycle(self):
        biclycle = Bicycle.objects.create(brand='BMX',
                                          serial='ABC123456')
        response = self.c.get('/bicycle/list/')
        self.assertEqual(response.status_code, 200)

    def test_for_one_biclycle(self):
        biclycle = Bicycle.objects.create(brand='BMX',
                                          serial='ABC123456')
        response = self.c.get('/bicycle/list/?brand={biclycle.brand}')
        self.assertEqual(response.status_code, 200)



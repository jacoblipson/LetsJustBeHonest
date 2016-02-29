from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from .models import Politician, Statement


class PoliticianTests(TestCase):
    def setUp(self):
        self.p1 = Politician.objects.create(
            first_name='George', last_name='Washington'
        )

    def tearDown(self):
        self.p1.delete()

    def test_politician_has_name(self):
        self.assertEqual(self.p1.first_name, 'George')
        self.assertEqual(self.p1.last_name, 'Washington')


class StatementTests(TestCase):
    def setUp(self):
        self.p1 = Politician.objects.create(last_name='Adams')
        self.s1 = Statement.objects.create(speaker=self.p1)

    def tearDown(self):
        self.s1.delete()
        self.p1.delete()

    def test_statement_has_speaker(self):
        self.assertEqual(self.s1.speaker, self.p1)

    def test_can_get_all_statements_by_politician(self):
        self.assertEqual(len(self.p1.statements.all()), 1)
        self.assertEqual(self.p1.statements.first(), self.s1)


class PoliticianListAPITests(APITestCase):
    def setUp(self):
        self.url = '/api/politicians/list/'
        self.client = APIClient()
        self.pol1 = Politician.objects.create(slug='richard-nixon',
                                              party='Republican',
                                              roles='Party Leader, Senator')
        self.pol2 = Politician.objects.create(slug='bill-clinton',
                                              party='Democrat',
                                              roles='Party Leader')

    def tearDown(self):
        self.pol1.delete()
        self.pol2.delete()

    def test_api_returns_all_politicians_by_default(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), Politician.objects.count())

    def test_api_filters_by_party(self):
        data = {'roles': 'Party Leader'}

        response = self.client.get(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

        data['party'] = 'Democrat'
        response = self.client.get(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['slug'], self.pol2.slug)

from django.test import TestCase

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
        self.p1 = Statement.objects.create(last_name='Adams')
        self.s1 = Statement.objects.create(speaker=self.p1)

    def tearDown(self):
        self.s1.delete()
        self.p1.delete()

    def test_statement_has_speaker(self):
        self.assertEqual(self.s1.speaker, self.p1)

    def test_can_get_all_statements_by_politician(self):
        self.assertEqual(len(self.p1.statements.all()), 1)
        self.assertEqual(self.p1.statements.first(), self.s1)

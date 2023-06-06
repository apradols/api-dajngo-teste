from django.test import TestCase
from aluraflix.models import Programa

class FixtureDataTestCase(TestCase):
    fixtures = ['programas_iniciais']

    def test_verify_fixture(self):
        programa_bizarro = Programa.objects.get(pk=1)
        programas = Programa.objects.all()
        self.assertEqual(programa_bizarro.titulo, 'Coisas bizarras')
        self.assertEqual(len(programas), 9)
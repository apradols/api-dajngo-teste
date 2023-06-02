from django.test import TestCase
from aluraflix.models import Programa

class ProramaModelsTestCase(TestCase):

    def setUp(self):
        self.programa = Programa(
            titulo = 'Procurando Nemo',
             data_lancamento = '2003-09-16'
        )

    def test_atributos(self):
        self.assertEquals(self.programa.titulo, 'Procurando Nemo')        
        self.assertEquals(self.programa.tipo, 'F')
        self.assertEquals(self.programa.data_lancamento, '2003-09-16')
        self.assertEquals(self.programa.likes, 0)
        self.assertEquals(self.programa.dislikes, 0)

        
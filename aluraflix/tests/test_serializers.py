from django.test import TestCase
from aluraflix.serializers import ProgramaSerializer
from aluraflix.models import Programa


class ProgramaSerializersTestCase(TestCase):


    def setUp(self):
        self.programa = Programa(
             titulo = 'Procurando Nemo',
             data_lancamento = '2003-09-16',
             tipo = 'F',
             likes = 40,
             dislikes = 2
        )

        self.serializer = ProgramaSerializer(instance=self.programa)

    def test_campos_serializados(self):
        data = self.serializer.data
        self.assertEquals(set(data.keys()), set(['titulo','tipo', 'data_lancamento', 'likes']))

    def test_conteudo(self):
        data = self.serializer.data
        self.assertEquals(data['titulo'], self.programa.titulo)
        self.assertEquals(data['data_lancamento'], self.programa.data_lancamento)
        self.assertEquals(data['tipo'], self.programa.tipo)
        self.assertEquals(data['likes'], self.programa.likes)
import unittest
from modulos.gestores import Gestor_de_base_de_datos

#¿Cómo crear una base de datos de prueba?

class TestGestorBD(unittest.TestCase):
    
    def setUp(self):
        self.gestorBD = Gestor_de_base_de_datos() 

    def test_consultar_dato(self):
        """Prueba que devuelva el dato solicitado de la base de datos"""

    def test_modificar_dato(self):
        """Prueba que se modifique en la base de datos el dato solicitado"""
import unittest
from modulos.gestores import Gestor_de_reclamos
#from modulos.databases import *


class TestGestor(unittest.TestCase):
    
    def setUp(self):
        self.gestor = Gestor_de_reclamos() 

    def test_crear_reclamo(self):
        """Prueba la correcta creación del reclamo con la información proporcionada por el usuario"""

    def test_asignar_a_depto(self):
        """Prueba que se asigne al departamento correspondiente"""
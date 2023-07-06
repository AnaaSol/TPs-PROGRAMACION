import unittest
from modulos.classes import *
#from modulos.databases import *

class TestReclamo(unittest.TestCase):
    
    def setUp(self):
        self.reclamo = Reclamo() 

    def test_sumar_adherente(self):
        """Prueba que se guarden los usuarios adheridos"""

    def test_cambiar_estado(self):
        """Prueba que se cambie correctamente el estado del reclamo"""

    def test_set_depto(self):
        """Prueba que se derive al departamento correcto después de la clasificación"""
import unittest
from modulos.classes import *
#from modulos.databases import *

class TestUsuario(unittest.TestCase):
    
    def setUp(self):
        self.usuario = Usuario() 

    def test_generar_reclamo(self):
        """Prueba la correcta generacion de un reclamo"""

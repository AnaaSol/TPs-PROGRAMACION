import unittest
from modules.jefe import Jefe
#from modulos.databases import *

class TestJefe(unittest.TestCase):
    
    def setUp(self):
        self.jefe = Jefe(1, "Ana Sol", "Murzi", "anam28", "anas.murzi@gmail.com", "contraseña", "maestranza")

    def test_get_depto(self):
        """Prueba la correcta obtencion del departamento"""
        self.assertEqual(self.jefe.get_departamento(), "maestranza")

    def test_set_depto(self):
        """Prueba que cambie el departamento"""
        self.jefe.set_departamento("secretaría técnica")
        self.assertEqual(self.jefe.get_departamento(), "secretaría técnica")

    


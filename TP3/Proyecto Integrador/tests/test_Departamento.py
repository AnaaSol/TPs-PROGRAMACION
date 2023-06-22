import unittest
from modulos.classes import *
#from modulos.databases import *

class TestDepartamento(unittest.TestCase):
    
    def setUp(self):
        self.depto = Departamento() 

    def test_algo(self):
        """Prueba"""
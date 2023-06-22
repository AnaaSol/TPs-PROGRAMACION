import unittest
from modulos.classes import *
#from modulos.databases import *

class TestJefe(unittest.TestCase):
    
    def setUp(self):
        self.jefe = Jefe() 

    def test_algo(self):
        """Prueba"""
import unittest
from modulos.classes import *
#from modulos.databases import *

class TestReclamo(unittest.TestCase):
    
    def setUp(self):
        self.reclamo = Reclamo() 

    def test_algo(self):
        """Prueba"""
import unittest
from modulos.classes import *
#from modulos.databases import *

class TestSecretario(unittest.TestCase):
    
    def setUp(self):
        self.secretario = Secretario() 

    def test_derivar_reclamo(self):
        """Prueba la correcta derivación de un reclamo mal-clasificado"""
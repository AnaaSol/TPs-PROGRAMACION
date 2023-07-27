import unittest
import datetime
from modules.reclamo import Reclamo
#from modulos.databases import *

class TestReclamo(unittest.TestCase):
    
    def setUp(self):
        self.reclamo= Reclamo(1, "No hay agua en el baño", str(datetime.datetime.now())[:19], 1) 

    def test_sumar_adherente(self):
        """Prueba que se guarden los usuarios adheridos"""

        self.reclamo.sumar_adherente(2)
        self.assertEqual(self.reclamo.get_adherentes, [2])


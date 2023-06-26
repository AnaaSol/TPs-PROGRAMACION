import unittest
from modulos.classes import *
#from modulos.databases import *

class TestJefe(unittest.TestCase):
    
    def setUp(self):
        self.jefe = Jefe()
        self.reclamo= Reclamo() 

    def test_manejar_reclamo(self):
        """Prueba que actualice el estado del reclamo"""

    def test_generar_reporte(self):
        """Prueba la correcta generación del reporte (con los gráficos y estadísticas solicitadas)"""

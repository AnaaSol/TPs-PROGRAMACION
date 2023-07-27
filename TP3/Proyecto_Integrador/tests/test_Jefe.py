import unittest
from modules.jefe import Jefe
#from modulos.databases import *

class TestJefe(unittest.TestCase):
    
    def setUp(self):
        self.jefe = Jefe(1, "Ana Sol", "Murzi", "anam28", "anas.murzi@gmail.com", "contraseña", "maestranza")

    def test_manejar_reclamo(self):
        """Prueba que actualice el estado del reclamo"""

    def test_generar_reporte(self):
        """Prueba la correcta generación del reporte (con los gráficos y estadísticas solicitadas)"""

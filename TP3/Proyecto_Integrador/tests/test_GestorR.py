import unittest
from modules.gestores import Gestor_de_reclamos
from modules.reclamo import Reclamo
#from modulos.databases import *

class TestGestor(unittest.TestCase):
    
    def setUp(self):
        self.gestor = Gestor_de_reclamos('data\clasificador_svm.pkl') 

    def test_crear_reclamo(self):
        """Prueba la correcta creación del reclamo con la información proporcionada"""

        data=[1, "Los pisos están suciones", "2023-07-26 16:14:36", 1]
        reclamo=self.gestor.crear_reclamo(data)
        print(reclamo.get_ID, data[0])
        self.assertEqual(str(reclamo.get_descripcion()), data[1])
        self.assertEqual(int(reclamo.get_ID()), data[0])
        self.assertEqual(str(reclamo.get_fecha()),  data[2])
        self.assertEqual(int(reclamo.get_ID_usuario()), data[3])

    def test_clasificar_reclamo(self):
        """Prueba que se asigne al departamento correspondiente"""

        reclamo2=self.gestor.crear_reclamo([1, "No funciona el campus virtual", "2023-07-26 16:14:36", 1])
        self.gestor.clasificar_reclamo(reclamo2)
        self.assertNotEqual(reclamo2.get_departamento, "")

    def test_filtrar_por_depto(self):
        """Prueba que funcione correctamente el filtro"""

        reclamo=Reclamo(1, "No hay papel", "2023-07-26 16:14:36", 1)
        reclamo2=Reclamo(2, "No hay wifi", "2023-07-26 16:14:36", 2)
        reclamo.set_depto("maestranza")
        reclamo2.set_depto("soporte informático")

        reclamos=[reclamo, reclamo2]

        filtro=self.gestor.filtrar_por_depto(reclamos, "maestranza")
        filtro2=self.gestor.filtrar_por_depto(reclamos, "soporte informático")

        self.assertEqual(reclamo, filtro)
        self.assertEqual(reclamo2, filtro2)




        
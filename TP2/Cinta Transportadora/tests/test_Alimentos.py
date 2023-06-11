import unittest
import random
from modulos.classes import Kiwi, Manzana, Papa, Zanahoria

class TestKiwi(unittest.TestCase):
    
    def setUp(self):
        self.kiwi = Kiwi(0.55) 
        self.awk=0.95999 #calculado
        self.random=[]
        self.kiwis=[]
    
    def test_calcular_aw(self):
        """Prueba el cálculo correcto de la actividad acuosa de kiwis"""

        #Se prueba el cálculo correcto del aw de un kiwi 
        self.assertAlmostEqual(self.kiwi.Calcular_aw(), self.awk, places=2)

        #Se prueba que el aw nunca sea mayor a 1
        for i in range(5):
            x=random.uniform(0.1,0.7)
            self.random.append(x)

        for i in self.random:
            un_kiwi=Kiwi(i)
            self.kiwis.append(un_kiwi)

        for kiwi in self.kiwis:
            kiwi.Calcular_aw()
            assert(kiwi.Calcular_aw()<0.99)

    def crear_kiwi(self):
        """Prueba que no se creen alimentos con pesos nulo o negativo"""

        imposible=Kiwi(0)
        imposible2=Kiwi(-10)
        self.assertRaises(imposible.control, imposible)
        self.assertRaises(imposible2.control, imposible2)        

class TestManzana(unittest.TestCase):
    
    def setUp(self):
        self.manzana = Manzana(0.35) 
        self.awm=0.93604 #calculado
    
    def test_calcular_aws(self):
        """Prueba el cálculo correcto del promedio de la actividad acuosa de manzanas"""

        #Se prueba el cálculo correcto del aw de una manzana
        self.assertAlmostEqual(self.manzana.Calcular_aw(), self.awm, places=2)

class TestZanahoria(unittest.TestCase):
    
    def setUp(self):
        self.zanahoria = Zanahoria(0.3) 
        self.awz=0.91220441 #calculado

    def test_calcular_aws(self):
        """Prueba el cálculo correcto del promedio de la actividad acuosa de zanahorias"""

        #Se prueba el cálculo correcto del aw de una zanahoria
        self.assertAlmostEqual(self.zanahoria.Calcular_aw(), self.awz, places=2)

class TestPapa(unittest.TestCase):
    
    def setUp(self):
        self.papa = Papa(0.6) 
        self.awp=0.97579 #calculado
    
    def test_calcular_aws(self):
        """Prueba el cálculo correcto del promedio de la actividad acuosa de papas"""

        #Se prueba el cálculo correcto del aw de una papa
        self.assertAlmostEqual(self.papa.Calcular_aw(), self.awp, places=2)

if __name__ == '__main__':
    
    unittest.main()
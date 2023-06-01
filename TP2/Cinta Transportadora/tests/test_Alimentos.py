import unittest
from modulos.classes import Kiwi, Manzana, Papa, Zanahoria

class TestKiwi(unittest.TestCase):
    
    def setUp(self):
        self.kiwi = Kiwi(0.55) 
    
    def test_calcular_aw(self):
        """Prueba el cálculo correcto de la actividad acuosa de kiwis"""

        #Se prueba el cálculo correcto del aw de un kiwi 
        awk=0.95999 #calculado
        self.assertAlmostEqual(self.kiwi.Calcular_aw(), awk, places=2)
        

class TestManzana(unittest.TestCase):
    
    def setUp(self):
        self.manzana = Manzana(0.35) 
    
    def test_calcular_aws(self):
        """Prueba el cálculo correcto del promedio de la actividad acuosa de kiwis, manzanas, zanahorias, papas, frutas, verduras, y alimentos"""

        #Se prueba el cálculo correcto del aw de una manzana
        awm=0.93604 #calculado
        self.assertAlmostEqual(self.manzana.Calcular_aw(), awm, places=2)

class TestZanahoria(unittest.TestCase):
    
    def setUp(self):
        self.zanahoria = Zanahoria(0.3) 
    
    def test_calcular_aws(self):
        """Prueba el cálculo correcto del promedio de la actividad acuosa de kiwis, manzanas, zanahorias, papas, frutas, verduras, y alimentos"""

        #Se prueba el cálculo correcto del aw de una zanahoria
        awz=0.95999 #calculado
        self.assertAlmostEqual(self.zanahoria.Calcular_aw(), awz, places=2)

class TestPapa(unittest.TestCase):
    
    def setUp(self):
        self.papa = Papa(0.6) 
    
    def test_calcular_aws(self):
        """Prueba el cálculo correcto del promedio de la actividad acuosa de kiwis, manzanas, zanahorias, papas, frutas, verduras, y alimentos"""

        #Se prueba el cálculo correcto del aw de una papa
        awp=0.97579 #calculado
        self.assertAlmostEqual(self.papa.Calcular_aw(), awp, places=2)

if __name__ == '__main__':
    
    unittest.main()
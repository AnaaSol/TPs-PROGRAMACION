import unittest
from modulos.classes import Cinta

class TestCinta(unittest.TestCase):
    
    def setUp(self):
        self.cinta = Cinta() 

    def test_Llenar_cajón(self):
        """Prueba que se llene correctamente un cajón (con el número de alimentos ingresado y sin alimentos no identificados)"""
        
        #Prueba llenar cajones con distinta cantidad de alimentos
        print(self.cinta.Llenar_cajón(8))
        print(self.cinta.Llenar_cajón(10))
        print(self.cinta.Llenar_cajón(20))
    
if __name__ == '__main__':
    
    unittest.main()
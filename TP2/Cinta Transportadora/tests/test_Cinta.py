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
    
    def test_Separar(self):
        """Prueba que se separe correctamente un cajón"""

        #Prueba que los cajones de prueba se separen correctamente en kiwis, manzanas, zanahorias y papas
        cajón1=self.cinta.Llenar_cajón(10)
        cajón2=self.cinta.Llenar_cajón(25)
        cajón3=self.cinta.Llenar_cajón(50)

        print(self.cinta.Separar(cajón1))
        print(self.cinta.Separar(cajón2))
        print(self.cinta.Separar(cajón3))

        #Prueba que se lanza una excepción cuando el cajón está vacío
        cajón_vacío=self.cinta.Llenar_cajón(0)
        self.cinta.Separar(cajón_vacío)

    #def test_Analizar_calidad(self):
    #    pass
    
if __name__ == '__main__':
    
    unittest.main()
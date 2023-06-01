import unittest
from modulos.classes import *

class TestCalculadora_aw(unittest.TestCase):
    
    def setUp(self):
        self.calculadora = Calculadora_Aw() 
    
    def test_calcular_aws(self):
        """Prueba el cálculo correcto del promedio de la actividad acuosa de kiwis, manzanas, zanahorias, papas, frutas, verduras, y alimentos"""

        #Se prueba el cálculo correcto del aw promedio de varios kiwis
        kiwi=Kiwi(0.12)
        kiwi2=Kiwi(0.3)
        kiwi3=Kiwi(0.09)
        cajón_de_kiwis=[kiwi, kiwi2, kiwi3]
        awk_prom=0.78521498 #calculado
        self.assertAlmostEqual(self.calculadora.Calcular_aws(cajón_de_kiwis)[0], awk_prom, places=2)

        #Se prueba el cálculo correcto del aw promedio de varias manzanas
        mzna=Manzana(0.3)
        mzna2=Manzana(0.35)
        mzna3=Manzana(0.3)
        cajón_de_manzanas=[mzna, mzna2, mzna3]
        awm_prom=0.92824842 #calculado
        self.assertAlmostEqual(self.calculadora.Calcular_aws(cajón_de_manzanas)[1], awm_prom, places=2)
        
        #Se prueba el cálculo correcto del aw promedio de varias zanahorias
        zana=Zanahoria(0.3)
        zana2=Zanahoria(0.45)
        zana3=Zanahoria(0.2)
        cajón_de_zanahorias=[zana, zana2, zana3]
        awz_prom=0.89720597 #calculado
        self.assertAlmostEqual(self.calculadora.Calcular_aws(cajón_de_zanahorias)[3], awz_prom, places=2)
        
        #Se prueba el cálculo correcto del aw promedio de varias papas
        papa=Papa(0.5)
        papa2=Papa(0.6)
        papa3=Papa(0.35)
        cajón_de_papas=[papa, papa2, papa3]
        awp_prom=0.95743682 #calculado
        self.assertAlmostEqual(self.calculadora.Calcular_aws(cajón_de_papas)[2], awp_prom, places=2)

        #Se prueba el cálculo correcto del aw promedio del total de alimentos
        zanahoria4=Zanahoria(0.3)
        papa4=Papa(0.5)
        kiwi4=Kiwi(0.3)
        manzana4=Manzana(0.2)
        cajón4=[zanahoria4, papa4, kiwi4, manzana4]
        awTot=(0.912204414+0.963691809+0.95136715+0.873)/4
        self.assertAlmostEqual(self.calculadora.Calcular_aws(cajón4)[6], awTot, places=2)

        #Prueba que se lanza una excepción cuando no hay alimentos (el cajón está vacío)
        cajón_vacío=[]
        #self.calculadora.Calcular_aws(cajón_vacío)
    
if __name__ == '__main__':
    
    unittest.main()
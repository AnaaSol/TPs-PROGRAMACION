import unittest
from modulos.classes import *

class TestCalculadora_aw(unittest.TestCase):
    
    def setUp(self):
        self.calculadora = Calculadora_Aw() 
        kiwi=Kiwi(0.12)
        kiwi2=Kiwi(0.3)
        kiwi3=Kiwi(0.09)
        self.cajón_de_kiwis=[kiwi, kiwi2, kiwi3]
        self.awk_prom=0.78521498 #calculado
        mzna=Manzana(0.3)
        mzna2=Manzana(0.35)
        mzna3=Manzana(0.3)
        self.cajón_de_manzanas=[mzna, mzna2, mzna3]
        self.awm_prom=0.92824842 #calculado
        zana=Zanahoria(0.3)
        zana2=Zanahoria(0.45)
        zana3=Zanahoria(0.2)
        self.cajón_de_zanahorias=[zana, zana2, zana3]
        self.awz_prom=0.89720597 #calculado
        papa=Papa(0.5)
        papa2=Papa(0.6)
        papa3=Papa(0.35)
        self.cajón_de_papas=[papa, papa2, papa3]
        self.awp_prom=0.95743682 #calculado
        zana4=Zanahoria(0.3)
        papa4=Papa(0.5)
        kiwi4=Kiwi(0.3)
        mzna4=Manzana(0.2)
        self.cajón4=[zana4, papa4, kiwi4, mzna4]
        self.awTot=(0.912204414+0.963691809+0.95136715+0.873)/4
    
    def test_calcular_aws(self):
        """Prueba el cálculo correcto del promedio de la actividad acuosa de kiwis, manzanas, zanahorias, papas, frutas, verduras, y alimentos"""

        #Se prueba el cálculo correcto del aw promedio de varios kiwis
        self.assertAlmostEqual(self.calculadora.Calcular_aw_prom(self.cajón_de_kiwis, Kiwi), self.awk_prom, places=2)

        #Se prueba el cálculo correcto del aw promedio de varias manzanas
        self.assertAlmostEqual(self.calculadora.Calcular_aw_prom(self.cajón_de_manzanas, Manzana), self.awm_prom, places=2)
        
        #Se prueba el cálculo correcto del aw promedio de varias zanahorias
        self.assertAlmostEqual(self.calculadora.Calcular_aw_prom(self.cajón_de_zanahorias, Zanahoria), self.awz_prom, places=2)
        
        #Se prueba el cálculo correcto del aw promedio de varias papas
        self.assertAlmostEqual(self.calculadora.Calcular_aw_prom(self.cajón_de_papas, Papa), self.awp_prom, places=2)

        #Se prueba el cálculo correcto del aw promedio del total de alimentos
        self.assertAlmostEqual(self.calculadora.Calcular_aw_prom(self.cajón4, Alimento), self.awTot, places=2)


    
if __name__ == '__main__':
    
    unittest.main()
import unittest
from modulos.classes import Calculadora_aw

class TestCalculadora_aw(unittest.TestCase):
    
    def setUp(self):
        self.calculadora = Calculadora_aw() 
    
    def test_calcular_aw(self):
        """Prueba el cálculo correcto de la actividad acuosa de kiwis, manzanas, zanahorias y papas"""

        #Se prueba el cálculo correcto del aw de un kiwi 
        kiwi=[{"alimento": "kiwi", "peso": 0.55}]
        awk=0.95999 #calculado
        self.assertAlmostEqual(self.calculadora.Calcular_aw(kiwi, "kiwi"), awk, places=2)

        #Se prueba el cálculo correcto del aw de una manzana
        manzana=[{"alimento": "manzana", "peso": 0.35}]
        awm=0.93604 #calculado
        self.assertAlmostEqual(self.calculadora.Calcular_aw(manzana, "manzana"), awm, places=2)

        #Se prueba el cálculo correcto del aw de una zanahoria
        zanahoria=[{"alimento": "zanahoria", "peso": 0.3}]
        awz=0.95999 #calculado
        self.assertAlmostEqual(self.calculadora.Calcular_aw(zanahoria, "zanahoria"), awz, places=2)

        #Se prueba el cálculo correcto del aw de una papa
        papa=[{"alimento": "papa", "peso": 0.6}]
        awp=0.97579 #calculado
        self.assertAlmostEqual(self.calculadora.Calcular_aw(papa, "papa"), awp, places=2)

        #Se prueba el cálculo correcto del aw promedio de varios kiwis
        cajón_de_kiwis=[{"alimento": "kiwi", "peso": 0.12}, {"alimento": "kiwi", "peso": 0.3}, {"alimento": "kiwi", "peso": 0.09}]
        awk_prom=0.78521498 #calculado
        self.assertAlmostEqual(self.calculadora.Calcular_aw(cajón_de_kiwis, "kiwi"), awk_prom, places=2)

        #Se prueba el cálculo correcto del aw promedio de varias manzanas
        cajón_de_manzanas=[{"alimento": "manzana", "peso": 0.3}, {"alimento": "manzana", "peso": 0.35}, {"alimento": "manzana", "peso": 0.3}]
        awm_prom=0.92824842 #calculado
        self.assertAlmostEqual(self.calculadora.Calcular_aw(cajón_de_manzanas, "manzana"), awm_prom, places=2)
        
        #Se prueba el cálculo correcto del aw promedio de varias zanahorias
        cajón_de_zanahorias=[{"alimento": "zanahoria", "peso": 0.3}, {"alimento": "zanahoria", "peso": 0.45}, {"alimento": "zanahoria", "peso": 0.2 }]
        awz_prom=0.89720597 #calculado
        self.assertAlmostEqual(self.calculadora.Calcular_aw(cajón_de_zanahorias, "zanahoria"), awz_prom, places=2)
        
        #Se prueba el cálculo correcto del aw promedio de varias papas
        cajón_de_papas=[{"alimento": "papa", "peso": 0.5}, {"alimento": "papa", "peso": 0.6}, {"alimento": "papa", "peso": 0.35}]
        awp_prom=0.95743682 #calculado
        self.assertAlmostEqual(self.calculadora.Calcular_aw(cajón_de_papas, "papa"), awp_prom, places=2)

        #Prueba que se lanza una excepción cuando el tipo de alimento ingresado y los alimentos del cajón no coinciden (o hay distintos tipos de alimentos en el cajón)
        cajón_mixto=[{"alimento": "kiwi", "peso": 0.02}, {"alimento": "papa", "peso": 0.30}, {"alimento": "manzana", "peso": 0.35}]
        self.calculadora.Calcular_aw(cajón_mixto, "kiwi")
        self.calculadora.Calcular_aw(cajón_mixto, "manzana")

        #Prueba que se lanza una excepción cuando no hay alimentos (el cajón está vacío)
        cajón_vacío=[]
        self.calculadora.Calcular_aw(cajón_vacío, "kiwi")

        #Prueba que se lanza una excepción cuando se quiere calcular la aw de un tipo de alimento con el que la calculadora no trabaja
        cajón=[{"alimento": "kiwi", "peso": 0.02}, {"alimento": "papa", "peso": 0.30}]
        self.calculadora.Calcular_aw(cajón, "zapallo")
        self.calculadora.Calcular_aw(cajón, "tomate")
        self.calculadora.Calcular_aw(cajón, "sandía")
    
    
if __name__ == '__main__':
    
    unittest.main()
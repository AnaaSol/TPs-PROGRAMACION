from math import *
import numpy as np
import random

class DetectorAlimento:
    """clase que representa un conjunto de sensores de la cinta transportadora
    para detectar el tipo de alimento y su peso.
    """
    def __init__(self):
        self.alimentos = ["kiwi", "manzana", "papa", "zanahoria", "undefined"]
        self.peso_alimentos = np.round(np.linspace(0.05, 0.6, 12),2)
        self.prob_pesos = np.round(self.__softmax(self.peso_alimentos)[::-1], 2)

    def __softmax(self, x):
        """función softmax para crear vector de probabilidades 
        que sumen 1 en total
        """
        return (np.exp(x - np.max(x)) / np.exp(x - np.max(x)).sum())

    def detectar_alimento(self):
        """método que simula la detección del alimento y devuelve un diccionario
        con la información del tipo y el peso del alimento.
        """
        n_alimentos = len(self.alimentos)
        alimento_detectado = self.alimentos[random.randint(0, n_alimentos-1)]
        peso_detectado = random.choices(self.peso_alimentos, self.prob_pesos)[0]
        return {"alimento": alimento_detectado, "peso": peso_detectado}
    
class Calculadora_aw():
    def Calcular_aw(self, alimentos, tipo):
        """Calcula la actividad acuosa de un conjunto de alimentos iguales"""
        #tipo es un str y alimentos es un cajón: una lista de diccionarios con las claves "alimento" y "peso"
        if tipo in ["kiwi", "manzana", "papa", "zanahoria"]:
            if len(alimentos)==0:
                raise Exception("No hay alimentos")
            else:
                tot=len(alimentos)
                aws=0
                for i in range(len(alimentos)):
                    if alimentos[i]["alimento"]==tipo:
                        if tipo=="kiwi":
                            peso=alimentos[i]["peso"]
                            aw=round(0.96*(1-(e)**((-1/18)*peso))/(1+(e)**((-1/18)*peso)), 3)
                            aws+=aw
                        elif tipo=="manzana":
                            peso=alimentos[i]["peso"]
                            aw=round(0.97*(((1/15)*peso)**2)/(1+((1/15)*peso)**2), 3)
                            aws+=aw
                        elif tipo=="zanahoria":
                            peso=alimentos[i]["peso"]
                            aw=round((0.96*(1*-e**(-1/10)*peso)), 3)
                            aws+=aw
                        elif tipo=="papa":
                            peso=alimentos[i]["peso"]
                            aw=round(0.66*atan((1/18)*peso), 3)
                            aws+=aw
                    else:
                        raise Exception("Los alimentos no son del mismo tipo")
                return aws/tot
        else:
            raise Exception("Lo sentimos, esta calculadora sólo puede trabajar con kiwis, manzanas, papas o zanahorias")

class Cinta():
    def __init__(self):
        self.sensor=DetectorAlimento()
        self.calculadora=Calculadora_aw()

    def Llenar_cajón(self, N):
        cajón=[]
        for i in range(N):
            cajón.append(self.sensor.detectar_alimento())

        for x in range(len(cajón)):
            while cajón[x]["alimento"]=="undefined":
                cajón[x]=self.sensor.detectar_alimento()

        return cajón

    def Separar(self, cajón):
        """Separa el contenido del cajón según el alimento"""
        kiwis=[]
        manzanas=[]
        zanahorias=[]
        papas=[]
        if len(cajón)==0:
            raise Exception("El cajón está vacío")
        else:
            for i in range(len(cajón)):
                if cajón[i]["alimento"]=="zanahoria":
                    zanahorias.append(cajón[i])
                elif cajón[i]["alimento"]=="papa":
                    papas.append(cajón[i])
                elif cajón[i]["alimento"]=="manzana":
                    manzanas.append(cajón[i])
                elif cajón[i]["alimento"]=="kiwi":
                    kiwis.append(cajón[i])
            return kiwis, manzanas, zanahorias, papas
        
    # def Analizar_calidad(self, kiwis, manzanas, zanahorias, papas):
    #     "Analiza la actividad acuosa de los alimentos en el cajón"
    #     awK=self.calculadora.Calcular_aw(kiwis, "kiwi")
    #     awM=self.calculadora.Calcular_aw(manzanas, "manzana")
    #     awP=self.calculadora.Calcular_aw(papas, "papa")
    #     awZ=self.calculadora.Calcular_aw(zanahorias, "zanahoria")
    #     #debería poner cada cálculo dentro de un try en caso de que el cajón no tenga el alimento y la calculadora devuelva que el cajón está vacío, pero no sé cómo referenciar esa excepción particular en el except
    #     awFrutas_prom=(awK+awM)/(len(M)+len(K))
    #     awVerduras_prom=(awP+awZ)/(len(P)+len(Z))
    #     if awK>0.95:
    #         print("Se recomienda revisar los kiwis")
        
    #     if awM>0.95:
    #         print("Se recomienda revisar las manzanas")

    #     if awP>0.95:
    #         print("Se recomienda revisar las papas")

    #     if awZ>0.95:
    #         print("Se recomienda revisar las zanahorias")

    #     if awZ<=0.95 and awM<=0.95 and awK<=0.95 and awP<=0.95:
    #         print("Todo correcto")

    #     return awM, awK, awFrutas_prom, awZ, awP, awVerduras_prom


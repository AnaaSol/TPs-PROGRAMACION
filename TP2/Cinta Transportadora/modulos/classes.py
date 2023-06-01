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
    
class Calculadora_Aw():
    """Calcula el promedio de la aw de un cajón por alimento y tipo de alimento"""
    def Calcular_aws(self, cajón):
   
        if len(cajón)==0:
            raise Exception("El cajón está vacío")
        else: 
            awk=0
            kiwis=0
            awm=0
            manzanas=0
            awp=0
            papas=0
            awz=0
            zanahorias=0
            awFrutas=0
            awVerduras=0
            awTot=0

            for alimento in cajón:
                aw=alimento.Calcular_aw()
                awTot+=aw
                if isinstance(alimento, Kiwi):
                    kiwis+=1
                    awk+=aw
                    awFrutas+=aw
                if isinstance(alimento, Manzana):
                    manzanas+=1
                    awm+=aw
                    awFrutas+=aw
                if isinstance(alimento, Papa):
                    papas+=1
                    awp+=aw
                    awVerduras+=aw
                if isinstance(alimento, Zanahoria):
                    zanahorias+=1
                    awz+=aw
                    awVerduras+=aw

            if zanahorias==0:
                awz_prom=0
            else:
                awz_prom=awz/zanahorias

            if papas==0:
                awp_prom=0
            else:
                awp_prom=awp/papas

            if kiwis==0:
                awk_prom=0
            else:
                awk_prom=awk/kiwis

            if manzanas==0:
                awm_prom=0
            else:
                awm_prom=awm/manzanas

            if kiwis+manzanas==0:
                awFrutas=0
            else:
                awFrutas=awFrutas/(kiwis+manzanas)

            if papas+zanahorias==0:
                awVerduras=0
            else:
                awVerduras=awVerduras/(papas+zanahorias)

            return awk_prom, awm_prom, awp_prom, awz_prom, awFrutas, awVerduras, awTot/(manzanas+kiwis+papas+zanahorias)


class Cinta():
    def __init__(self):
        self.sensor=DetectorAlimento()

    def Llenar_cajón(self, N):
        lista=[]
        cajón=[]
        for i in range(N):
            lista.append(self.sensor.detectar_alimento())

        for x in range(len(cajón)):
            while lista[x]["alimento"]=="undefined":
                lista[x]=self.sensor.detectar_alimento()
  
        for dato in lista:
            if dato["alimento"]=="kiwi":
                kiwi=Kiwi(dato["peso"])
                cajón.append(kiwi)
            elif dato["alimento"]=="manzana":
                manzana=Manzana(dato["peso"])
                cajón.append(manzana)
            elif dato["alimento"]=="zanahoria":
                zanahoria=Zanahoria(dato["peso"])
                cajón.append(zanahoria)
            elif dato["alimento"]=="papa":
                papa=Papa(dato["peso"])
                cajón.append(papa)

        return cajón
        
class Alimento():
    def __init__(self, peso):
        self.peso=peso

class Kiwi(Alimento):
    def Calcular_aw(self):
        aw=round(0.96*(1-(e)**((-18)*self.peso))/(1+(e)**((-18)*self.peso)), 3)
        return aw

class Manzana(Alimento):
    def Calcular_aw(self):
        aw=round(0.97*(((15)*self.peso)**2)/(1+((15)*self.peso)**2), 3)
        return aw

class Papa(Alimento):
    def Calcular_aw(self):
        aw=round(0.66*atan((18)*self.peso), 3)
        return aw

class Zanahoria(Alimento):
    def Calcular_aw(self):
        aw=round((0.96*(1*-e**(-10)*self.peso)), 3)
        return aw

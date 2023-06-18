from math import *
import numpy as np
import random
from abc import ABC, abstractmethod

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
    
    def Calcular_aw_prom(self, cajón, tipo):
        aws=0
        cant=0
        for alimento in cajón:
            if isinstance(alimento, tipo):
                aws+=alimento.Calcular_aw()
                cant+=1
        if cant!=0:
            return round(aws/cant, 2)
        else:
            return aws
        

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
        
class Alimento(ABC):

    def __init__(self, peso):
        self.peso=self.__control(peso)

    def __control(self, peso):
        if peso>0:
            self.peso=peso
            return self.peso
        else:
            raise Exception ("No se puede crear el alimento")

    @abstractmethod
    def Calcular_aw(self):
        pass

class Fruta(Alimento, ABC):
    @abstractmethod
    def Calcular_aw(self):
        pass

class Verdura(Alimento, ABC):
    @abstractmethod
    def Calcular_aw(self):
        pass

class Kiwi(Fruta):
    def Calcular_aw(self):
        aw=round(0.96*(1-(e)**((-18)*self.peso))/(1+(e)**((-18)*self.peso)), 3)
        return aw

class Manzana(Fruta):
    def Calcular_aw(self):
        aw=round(0.97*(((15)*self.peso)**2)/(1+((15)*self.peso)**2), 3)
        return aw

class Papa(Verdura):
    def Calcular_aw(self):
        aw=round(0.66*atan((18)*self.peso), 3)
        return aw

class Zanahoria(Verdura):
    def Calcular_aw(self):
        aw=round(0.96*(1-exp(-10*self.peso)), 3)
        return aw

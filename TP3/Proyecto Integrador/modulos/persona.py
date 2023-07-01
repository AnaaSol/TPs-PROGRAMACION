from abc import ABC, abstractmethod

class Persona(ABC):
    
    @abstractmethod #los atributos son protegidos porque sino Usuario() y Jefe() no pueden acceder a ellos
    def __init__(self, ID, nombre, apellido, usuario, email, contraseña):
        self._ID=ID #¿cómo asegurar que sea única?
        self._nombre=nombre
        self._apellido=apellido
        self._usuario=usuario
        self._contraseña=contraseña
        self._email=email

    #setters: compilados en la función cambiar_datos()

    def cambiar_datos(self, dato_a_cambiar, nuevo):
        #debería pedir la contraseña antes de permtiir hacer cambios: controlado desde el HTML
        if dato_a_cambiar == "email":
            #debería chequear que el mail no esté ocupado
            self._mail=nuevo
        elif dato_a_cambiar == "contraseña":
            self._contraseña=nuevo
    
    # def cambiar_contraseña(self, contraseña, contraseña_nueva):
    #     if contraseña==self.__contraseña:
    #         self.__contraseña=contraseña_nueva
    #     else:
    #         return "La contraseña ingresada no coincide."

    #getters

    def get_nombre(self):
        return self._nombre

    def get_apellido(self):
        return self._apellido
    
    def get_usuario(self):
        return self._usuario

    def get_contraseña(self):
        return self._contraseña

    def get_email(self):
        return self._email

#Galileo=Usuario()
#Galileo.contraseña=ksjdsk
#Galileo.set_contraseña(kajsks)
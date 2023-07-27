from abc import ABC, abstractmethod

class Persona(ABC):
    
    @abstractmethod #los atributos protegidos y no privados porque sino Usuario() y Jefe() no pueden acceder a ellos
    def __init__(self, ID, nombre, apellido, usuario, email, contraseña):
        self._ID=ID 
        self._nombre=nombre
        self._apellido=apellido
        self._usuario=usuario
        self._contraseña=contraseña
        self._email=email

    #setters: compilados en la función actualizar_datos()

    def actualizar_datos(self, contraseña, dato_a_cambiar, nuevo):
        """Con la contraseña correcta provista, actualiza el dato requerido"""
        if contraseña==self._contraseña:
            if dato_a_cambiar=="nombre":
                self._nombre=nuevo
            elif dato_a_cambiar=="apellido":
                self._apellido=nuevo
            elif dato_a_cambiar=="email":
                self._email=nuevo
            elif dato_a_cambiar=="contraseña":
                self._contraseña=nuevo
            else:
                raise Exception("Ese dato no existe o no puede modificarse")
        else:
            raise Exception("Contraseña incorrecta")

    #getters

    def get_ID(self):
        return self._ID

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
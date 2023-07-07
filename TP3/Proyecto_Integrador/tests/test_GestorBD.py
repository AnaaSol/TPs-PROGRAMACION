import unittest
from modulos.gestores import Gestor_de_base_de_datos

#¿Cómo crear una base de datos de prueba?

class TestGestorBD(unittest.TestCase):
    
    def setUp(self):
        self.gestorBD = Gestor_de_base_de_datos() 

    def test_get_dato_user(self, username, dato):
        """Prueba la correcta consulta del dato requerido"""
        password=self.gestorBD.get_dato_user("marip", "password")
        self.assertEqual(password, "blabla")
        email=self.gestorBD.get_dato_user("lucab", "email")
        self.assertEqual(email, "lucab@gmail.com")

        """Prueba las excepciones"""
        #dato inválido
        #invalid=self.gestorBD.get_dato_user("robert3", "birthdate")
        self.assertRaises(Exception, self.gestorBD.get_dato_user, "robert3", "birthdate")

        #user no existe 
        """Recibe el nombre de usuario y el dato a consultar y devuelve el valor del mismo, si el usuario existe y el dato es válido"""
        if dato in ["ID", "email", "username", "password", "name", "surname", "depto", "claustro", "reclamos_adheridos", "reclamos_generados"]:
            user=self.__get_user_by_username(username)
            attribute=getattr(user, dato, None)
            return attribute
        else:
            raise Exception("El dato ingresado no corresponde a ningún atributo de user")
        



    def test_modificar_dato(self):
        """Prueba que se modifique en la base de datos el dato solicitado"""
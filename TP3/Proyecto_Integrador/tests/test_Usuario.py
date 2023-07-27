import unittest
import datetime
from modules.usuario import Usuario
#from modulos.databases import *

class TestUsuario(unittest.TestCase):
    
    def setUp(self):
        self.usuario = Usuario(1, "Paula", "Demartini", "pau89", "paud@gmail.com", "contraseña", "estudiante") 

    def test_actualizar_datos(self):
        """Prueba el método actualizar_datos() y sus excepciones"""

        #se prueba la actualización del dato requerido
        self.usuario.actualizar_datos("contraseña", "nombre", "Belén")
        self.assertEqual(self.usuario.get_nombre(), "Belén")

        #se prueban las excepciones
        with self.assertRaises(Exception) as context:
            self.usuario.actualizar_datos("contraseña_incorrecta", "nombre", "Belén") 
            self.assertEqual(str(context.exception), "Contraseña incorrecta")

        with self.assertRaises(Exception) as context:
            self.usuario.actualizar_datos("contraseña", "edad", 10)
            self.assertEqual(str(context.exception), "Ese dato no existe o no puede modificarse")

    def test_generar_datos_reclamo(self):
        """Prueba el método generar_datos_reclamo(), es decir, la correcta creación del formulario para crear un reclamo"""
        
        formulario=self.usuario.generar_datos_reclamo("Programación Avanzada es muy difícil")
        momento=str(datetime.datetime.now())[:19]
        self.assertEqual(formulario[0], "Programación Avanzada es muy difícil")
        self.assertEqual(formulario[1], momento)
        self.assertEqual(formulario[2], self.usuario.get_ID())

    def test_adherirse_a_reclamo(self):
        """Prueba el método adherirse_a_reclamo(), es decir, la correcta adhesión a un reclamo por única vez"""

        #se prueba la adhesión a un reclamo
        self.usuario.adherirse_a_reclamo(1)
        self.assertEqual(self.usuario.get_reclamos_adheridos(), [1])

        #se prueba la excepción

        with self.assertRaises(Exception) as context:
            self.usuario.adherirse_a_reclamo(1)
        self.assertEqual(str(context.exception), "Usted ya está adherido a este reclamo")





    

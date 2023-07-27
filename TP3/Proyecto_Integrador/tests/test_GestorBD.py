import unittest
from modules.gestores import Gestor_de_base_de_datos
from modules.config import app, db
from modules.databases import Persona_db
    
class TestGestorBD(unittest.TestCase):
    
    def setUp(self):
        self.gestorBD = Gestor_de_base_de_datos() 

    def test_get_reclamos_by_filtro(self):
        """Prueba el método get_reclamos_by_filtro() y sus excepciones"""

        with app.test_request_context():
            db.create_all()

            #se prueban las excepciones
            with self.assertRaises(Exception) as context:
                self.gestorBD.get_reclamos_by_filtro("ID", 0) #el reclamo no existe
            self.assertEqual(str(context.exception), "El reclamo no existe") #verifica el mensaje de la excepción generada

            with self.assertRaises(Exception) as context:
                self.gestorBD.get_reclamos_by_filtro("fecha", "2023-07-26 16:14:36") #filtro inválido
            self.assertEqual(str(context.exception), "Sólo puede filtrar por usuario, departamento, estado o ID")

    def test_chequear_disponibilidad(self):
        """Prueba el método chequear_disponibilidad(), es decir, la correcta devolución de la disponibilidad del dato consultado en la bd"""

        with app.test_request_context():
            db.create_all()

            result=self.gestorBD.chequear_disponibilidad("email", "marip@gmail.com")
            self.assertEqual(result, "Email/usuario ocupado")

            result=self.gestorBD.chequear_disponibilidad("username", "feriado")
            self.assertEqual(result, "Email/usuario disponible")

    def test_get_dato_user(self):
        """Prueba el método get_dato_user() y sus excepciones"""

        with app.test_request_context():
            db.create_all()

            #se prueba la correcta consulta del dato requerido con valores conocidos (jefes)
            password=self.gestorBD.get_dato_user("marip", "password")
            email=self.gestorBD.get_dato_user("lucab", "email")
            self.assertEqual(email, "lucab@gmail.com")
            self.assertEqual(password, "blabla")

            #se prueban las excepciones
            with self.assertRaises(Exception) as context:
                self.gestorBD.get_dato_user("robert3", "birthdate") #filtro inválido
                self.assertEqual(str(context.exception), "El dato ingresado no corresponde a ningún atributo de user")

            with self.assertRaises(Exception) as context:
                self.gestorBD.get_dato_user("salamanca", "email")
                self.assertEqual(str(context.exception), "El usuario no existe")

    def test_modificar_dato(self):
        """Se prueba el método modificar_dato() y sus excepciones"""

        with app.test_request_context():
            db.create_all()

            #se prueban las excepciones
            with self.assertRaises(Exception) as context:
                self.gestorBD.modificar_dato("email", "grey@gmail.com", "jefe", 1)
                self.assertEqual(str(context.exception), "No existe una base de datos para esa clase o no se permite modificarla")
            
            with self.assertRaises(Exception) as context:
                self.gestorBD.modificar_dato("apellido", "Musk", "usuario", 1)
                self.assertEqual(str(context.exception), "No puede modificar este atributo del usuario")

            with self.assertRaises(Exception) as context:
                self.gestorBD.modificar_dato("fecha", "2023-07-26 16:14:36", "reclamo", 1)
                self.assertEqual(str(context.exception), "No puede modificar este atributo del reclamo")
        
    def test_guardar_nuevo_objeto(self):
        """Prueba el método guardar_nuevo_objeto() y sus excepciones"""

        with app.test_request_context():
            db.create_all()

            #se prueba que se guarde el objeto
            datos_nuevo_usuario=["Alan", "Torres", "provisorio@gmail.com", "usuarioprovisoriodeprueba", "caramelodelimón", "estudiante", "", ""]            
            self.gestorBD.guardar_nuevo_objeto("usuario", datos_nuevo_usuario)

            self.assertEqual(datos_nuevo_usuario[4], self.gestorBD.get_dato_user("usuarioprovisoriodeprueba", "password"))

            #se elimina el objeto una vez realizada la prueba
            objeto=db.session.query(Persona_db).filter_by(username="usuarioprovisoriodeprueba").one()
            db.session.delete(objeto)  
            db.session.commit()

            #se prueban las excepciones
            with self.assertRaises(Exception) as context:
                self.gestorBD.guardar_nuevo_objeto("estudiante", datos_nuevo_usuario)
                self.assertEqual(str(context.exception), "No existe esa base de datos")


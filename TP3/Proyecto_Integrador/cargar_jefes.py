#Esto debería estar en data
from modulos.config import app, db
from modulos.jefe_y_secretario import Jefe
from modulos.gestores import Gestor_de_base_de_datos

Jefe1=Jefe(0, "Mariano", "Pereira", "marip", "marip@gmail.com", "blabla", "secretaría técnica")
Jefe2=Jefe(0, "Luciana", "Cabrera", "lucab", "lucab@gmail.com", "tuqui", "maestranza")
Jefe3=Jefe(0, "Robertino", "Del Valle", "robert3", "robdv@gmail.com", "numpypy", "soporte informático")

datos_jefe1=[Jefe1.get_nombre(), Jefe1.get_apellido(), Jefe1.get_usuario(), Jefe1.get_email(), Jefe1.get_contraseña(), Jefe1.get_departamento()]
datos_jefe2=[Jefe2.get_nombre(), Jefe2.get_apellido(), Jefe2.get_usuario(), Jefe2.get_email(), Jefe2.get_contraseña(), Jefe2.get_departamento()]
datos_jefe3=[Jefe3.get_nombre(), Jefe3.get_apellido(), Jefe3.get_usuario(), Jefe3.get_email(), Jefe3.get_contraseña(), Jefe3.get_departamento()]

with app.app_context():
    db.create_all() #¿deberíamos crear la BD acá o en server?
    GestorDB=Gestor_de_base_de_datos()
    GestorDB.guardar_nuevo_objeto("jefe", datos_jefe1)
    GestorDB.guardar_nuevo_objeto("jefe", datos_jefe2)
    GestorDB.guardar_nuevo_objeto("jefe", datos_jefe3)
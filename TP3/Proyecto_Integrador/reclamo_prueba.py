from modulos.config import app, db
from modulos.gestores import Gestor_de_base_de_datos
import datetime

datos=["No hay papel higiénico en el módulo 1 durante toda la mañana", "pendiente", "maestranza", str(datetime.datetime.now())[:19], 6 ]

with app.app_context():
    db.create_all() #¿deberíamos crear la BD acá o en server?
    GestorDB=Gestor_de_base_de_datos()
    GestorDB.guardar_nuevo_objeto("reclamo", datos)
    print("Todo espectacular")
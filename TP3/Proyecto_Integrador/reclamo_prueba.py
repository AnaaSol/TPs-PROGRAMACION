from modulos.config import app, db
from modulos.databases import Reclamo_db
from modulos.gestores import Gestor_de_base_de_datos
import datetime

# datos=["No hay papel higiénico en el módulo 1 durante toda la mañana", "pendiente", "maestranza", str(datetime.datetime.now())[:19], 6 ]
# datos=["La señal de WiFi es muy baja en la sala de estudios", "pendiente", "soporte informático", str(datetime.datetime.now())[:19], 5]

with app.app_context():
    db.create_all() #¿deberíamos crear la BD acá o en server?
    # linea_a_eliminar = db.session.query(Reclamo_db).filter_by(ID_reclamo=2).first()
    # db.session.delete(linea_a_eliminar)
    # db.session.commit()
    # GestorDB=Gestor_de_base_de_datos()
    # GestorDB.guardar_nuevo_objeto("reclamo", datos)
    # print("Todo espectacular")
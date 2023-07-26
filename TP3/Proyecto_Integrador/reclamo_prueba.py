from modules.config import app, db
from modules.databases import Reclamo_db, Persona_db
from modules.gestores import Gestor_de_base_de_datos
import datetime

# datos=["No hay papel higiénico en el módulo 1 durante toda la mañana", "pendiente", "maestranza", str(datetime.datetime.now())[:19], 4 ]
# datos=["La señal de WiFi es muy baja en la sala de estudios", "pendiente", "soporte informático", str(datetime.datetime.now())[:19], 5]

with app.app_context():
    db.create_all() #¿deberíamos crear la BD acá o en server?
    # linea_a_eliminar = db.session.query(Reclamo_db).filter_by(ID_reclamo=1).first()
    # db.session.delete(linea_a_eliminar)
    # db.session.commit()
    # linea_a_eliminar = db.session.query(Persona_db).filter_by(ID=1).first()
    # db.session.delete(linea_a_eliminar)
    # db.session.commit()
    # GestorDB=Gestor_de_base_de_datos()
    # GestorDB.guardar_nuevo_objeto("reclamo", datos)
    # print("Todo espectacular")
    # claim=db.session.query(Reclamo_db).filter_by(ID_user=4).first()
    # print(claim.adherentes)
    
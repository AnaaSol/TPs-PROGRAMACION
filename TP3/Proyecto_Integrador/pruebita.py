from modules.config import app, db
from modules.gestores import Gestor_de_base_de_datos

Gestor=Gestor_de_base_de_datos()
with app.app_context():
    db.create_all()
    Gestor.modificar_dato("estado", "pendiente", "reclamo", 2)
from modules.config import app, db
from modules.databases import Persona_db, Reclamo_db

with app.app_context():
    db.create_all()
    reclamo_a_eliminar = db.session.query(Reclamo_db).filter_by(ID_reclamo=0).first()
    if reclamo_a_eliminar is not None:
        db.session.delete(reclamo_a_eliminar)
        db.session.commit()
from modules.config import app, db
from modules.databases import Reclamo_db

with app.app_context():
    db.create_all()
    reclamo_a_eliminar = db.session.query(Reclamo_db).filter_by(ID_reclamo=x).first()
    db.session.delete(reclamo_a_eliminar)
    db.session.commit()
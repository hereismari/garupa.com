from router import app
from core.database import db
    
with app.app_context():
    db.drop_all()
    db.create_all()

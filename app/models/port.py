from app.database import db

class Port(db.Model):
    __tablename__ = "ports"

    code = db.Column(db.Text, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    parent_slug = db.Column(db.Text, nullable=False)

from app.database import db


class Region(db.Model):
    __tablename__ = "regions"

    slug = db.Column(db.Text, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    parent_slug = db.Column(db.Text)
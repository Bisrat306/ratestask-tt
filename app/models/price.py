from app.database import db

class Price(db.Model):
    __tablename__ = "prices"

    orig_code = db.Column(db.Text, primary_key=True)
    dest_code = db.Column(db.Text, primary_key=True)
    day = db.Column(db.Date, primary_key=True)
    price = db.Column(db.Integer, nullable=False)


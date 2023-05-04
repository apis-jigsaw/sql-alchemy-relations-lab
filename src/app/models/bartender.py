from sqlalchemy.orm import relationship, backref
from app import db

class Bartender(db.Model):
    __tablename__ = 'bartenders'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    hometown = db.Column(db.String(120), unique=True, nullable=False)
    birthyear = db.Column(db.Integer(), unique=True, nullable=False)

    orders = relationship('Order', backref=backref('bartender'), cascade='all, delete-orphan')

    def __repr__(self):
        return '<User %r>' % self.name
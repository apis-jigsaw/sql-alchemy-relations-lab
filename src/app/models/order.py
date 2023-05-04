from app import db

class Order(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    bartender_id = db.Column(db.Integer(), db.ForeignKey('bartenders.id'))
    customer_id = db.Column(db.Integer(), db.ForeignKey('customers.id'))
    drink_id = db.Column(db.Integer(), db.ForeignKey('drinks.id'))

    def __repr__(self):
        return f'<Order id: {self.id}, customer_id: {self.customer_id}, drink_id: {self.drink_id}, bartender_id: {self.bartender_id}>'

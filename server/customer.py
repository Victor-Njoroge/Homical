from owner import db

class Customer(db.Model):
    __tablename__ = "customer"

    id=db.Column(db.Integer, primary_key=True)
    fname=db.Column(db.String, nullable=False)
    lname=db.Column(db.String, nullable=False)
    email=db.Column(db.String, nullable=False)
    phoneNo=db.Column(db.String, nullable=False)
    password=db.Column(db.String, nullable=False)

    booking=db.relationship('Bookings', backref='customer')
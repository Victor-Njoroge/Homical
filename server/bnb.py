from owner import db

class Bnb(db.Model):
    __tablename__ = "bnb"

    id=db.Column(db.Integer, primary_key=True)
    ownerId=db.Column(db.Integer, db.ForeignKey('owner.id'))
    name=db.Column(db.String, nullable=False)
    model=db.Column(db.String, nullable=False)
    location=db.Column(db.String, nullable=False)
    description=db.Column(db.String, nullable=False)
    address=db.Column(db.String, nullable=False)
    price=db.Column(db.String, nullable=False)
    likes=db.Column(db.Integer, default=0, nullable=True)

    booking=db.relationship('Bookings', backref='bnb')
    picture=db.relationship('Picture', backref='bnb')

    
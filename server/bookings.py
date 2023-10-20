from owner import db

class Bookings(db.Model):
    __tablename__ = 'bookings'

    id=db.Column(db.Integer, primary_key=True)
    bnbId=db.Column(db.Integer, db.ForeignKey('bnb.id'))
    customerId=db.Column(db.Integer,db.ForeignKey('customer.id'))
    checkin=db.Column(db.Date, nullable=False)
    checkout=db.Column(db.Date, nullable=False)
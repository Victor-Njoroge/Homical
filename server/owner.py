from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class Owner(db.Model):
    __tablename__ = "owner"

    id=db.Column(db.Integer, primary_key=True)
    fname=db.Column(db.String, nullable=False)
    lname=db.Column(db.String, nullable=False)
    phoneNo=db.Column(db.String, nullable=False)
    email=db.Column(db.String, nullable=False)
    password=db.Column(db.String, nullable=False)


    bnb=db.relationship('Bnb',backref='owner')
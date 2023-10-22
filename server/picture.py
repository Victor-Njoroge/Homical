from owner import db

class Picture(db.Model):
    __tablename__ = 'picture'

    id=db.Column(db.Integer, primary_key=True)
    url=db.Column(db.String, nullable=False)
    bnbId=db.Column(db.String, db.ForeignKey('bnb.id'))


    
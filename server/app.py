from flask import Flask
from flask_cors import CORS
from owner import Owner, db
from bnb import Bnb
from bookings import Bookings
from customer import Customer

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///mydatabase.db'
db.init_app(app)
CORS(app)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(port=5555, debug=True)
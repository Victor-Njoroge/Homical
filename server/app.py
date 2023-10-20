from flask import Flask,request,jsonify
from flask_cors import CORS
from owner import Owner, db
from bnb import Bnb
from bookings import Bookings
from customer import Customer

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///mydatabase.db'
db.init_app(app)
CORS(app)

@app.route('/create_customer', methods=["POST"])
def post_customer():
    if request.method == "POST":
        data=request.json

        if 'fname' in data and 'lname' in data and 'email' in data and 'phoneNo' in data and 'password' in data:
            new_customer= Customer(
                fname=str(data['fname']),
                lname=str(data['lname']),
                email=str(data['email']),
                phoneNo=str(data['phoneNo']),
                password=str(data['password'])
            )

            db.session.add(new_customer)
            db.session.commit()

            return jsonify({'message':'Customer account created successfully'}), 201
        else:
            return jsonify({'error':'Missing fields in the request data'}), 400

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(port=5555, debug=True)
from flask import Flask,request,jsonify
from flask_cors import CORS
from owner import Owner, db
from bnb import Bnb
from bookings import Bookings
from customer import Customer
from picture import Picture

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
        

@app.route('/create_owner', methods=["POST"])
def post_owner():
    if request.method == "POST":
        data = request.json
        
        if 'fname' in data and 'lname' in data and 'profilePic' in data and 'phoneNo' in data and 'email' in data and 'password' in data:
            new_owner=Owner(
                fname=str(data['fname']),
                lname=str(data['lname']),
                profilePic=str(data['profilePic']),
                phoneNo=str(data['phoneNo']),
                email=str(data['email']),
                password=str(data['password'])
            )

            db.session.add(new_owner)
            db.session.commit()

            return jsonify({"message":"Owner created successfully"}), 201
        
        else:
            return jsonify({"error":"Missing fields in the request data"}), 400


@app.route('/create_bnb', methods=["POST"])
def post_bnb():
    if request.method == "POST":
        data = request.json

        if 'ownerId' in data and 'name' in data and 'location' in data and 'model' in data and 'description' in data and 'address' in data and 'price' in data:
            new_bnb = Bnb(
                ownerId=data['ownerId'],
                name=data['name'],
                location=data['location'],
                description=data['description'],
                address=data['address'],
                price=data['price'],
                model=data['model']
            )

            db.session.add(new_bnb)
            db.session.commit()

            # Handle image URLs
            image_urls = data.get('imageUrls')

            if image_urls:
                for image_url in image_urls:
                    picture = Picture(url=image_url, bnbId=new_bnb.id)
                    db.session.add(picture)

                db.session.commit()

            return jsonify({"message": "BnB and image URLs created successfully"}), 201

        else:
            return jsonify({"error": "Missing fields in the request data"}), 400
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(port=5555, debug=True)
from flask import Flask
from flask_restful import Api, Resource, reqparse, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class CarModel(db.Model):
    make_model_year = db.Column(db.String(210), primary_key=True)
    make = db.Column(db.String(100))
    model = db.Column(db.String(100))
    year = db.Column(db.Integer)
    price = db.Column(db.Float)
    mileage = db.Column(db.Integer)

    def __repr__(self):
        return f"Car[make={make}, model={model}, year={year}, price={price}, mileage={mileage}]"

car_args = reqparse.RequestParser()
car_args.add_argument("make", type=str, required=True)
car_args.add_argument("model", type=str, required=True)
car_args.add_argument("year", type=int, required=True)
car_args.add_argument("price", type=float, required=True)
car_args.add_argument("mileage", type=int, required=True)


res_fields = {
    'make_model_year' : fields.String,
    'make' : fields.String,
    'model' : fields.String,
    'year' : fields.Integer,
    'price' : fields.Float,
    'mileage' : fields.Integer
}

class CarQuery(Resource):
    @marshal_with(res_fields)
    def get(self, specify):
        result = CarModel.query.filter_by(make_model_year=specify).first()
        return result

    @marshal_with(res_fields)
    def put(self, specify, track=False):
        result = self.get(specify).json()
        if result['make_model_year'] == None:
            args = car_args.parse_args()
            car = CarModel(make_model_year=specify, make=args['make'], model=args['model'], year=args['year'], price=args['price'], mileage=args['mileage'])
            db.session.add(car)
            db.session.commit()
            # if track:
                # implement the tracking script here

            return car, 201
        else:
            return result, 200
    def put(self, specify):
        args = car_args.parse_args()
        car = CarModel(make_model_year=specify, make=args['make'], model=args['model'], year=args['year'], price=args['price'], mileage=args['mileage'])
        db.session.add(car)
        db.session.commit()
        return car, 201
# find a better way to run this one time and then not run it again
#db.create_all()
api.add_resource(CarQuery, "/car_query/<string:specify>")

if __name__ == "__main__":
    # REMEMBER TO REMOVE WHEN FINISHED
    app.run(debug=True)

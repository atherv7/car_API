import requests, json
from flask_restful import reqparse
# import subprocess, os
class CarPrice:
    # class Car:
    #     def __init__(ma, mo, ye, mi, pr):
    #         self.make = ma
    #         self.model = mo
    #         self.year = ye
    #         self.mileage = mi
    #         self.price = pr

    def __init__(self, url='http://127.0.0.1:5000/'):
        # with open(os.devnull, 'w') as fh:
        #     cmd = subprocess.Popen("pythonw ../src/api.py", stdout=fh, stderr=fh)
        self.BASE = url

    def __repr__(self):
        return f"{self.year} {self.make} {self.model} with {self.mileage} miles : ${self.price}"

    def get_car(self, key):
        response = requests.get(self.BASE+'car_query/'+key)
        car = json.loads(response.text)
        #return CarPrice.Car(car["make"], car["model"], car["year"], car["mileage"], car["price"])
        return car

    def add_car(self, key, data, want_ret=False):
        response = requests.put(self.BASE+'car_query/'+key,data)
        if want_ret:
            car = json.loads(response.text)
            #return CarPrice.Car(car["make"], car["model"], car["year"], car["mileage"], car["price"])
            return car

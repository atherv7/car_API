import sys
sys.path.append('D:/Desktop/car_API_lib/src')

from library import CarPrice

search = CarPrice()
search.add_car('toyotaprius2003', {'make':'toyota', 'model':'prius', 'year':2003, 'mileage':100, 'price':500.00})
car = search.get_car('toyotaprius2003')
print(car)
search.add_car('toyotaprius2003', {'make':'toyota', 'model':'prius', 'year':2003, 'mileage':100, 'price':250.00})
car = search.get_car('toyotaprius2003')
print(car)

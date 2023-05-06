class Car:
    brand_name = "BMW"
    model = "Z4"
    manu_year = 2020

    def __init__(self,brand_name, model, manu_year):
        self.brand_name = brand_name
        self.model = model
        self.manu_year = manu_year

    def car_details(self):
        print("car brand is",self.brand_name)
        print("car model is", self.model)
        print("car manu year is ", self.manu_year)
    def get_car_brand(self):
        print("car brand is ", self.brand_name)



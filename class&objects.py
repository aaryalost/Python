
class Car:
   
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

   
    def display_details(self):
        print(f"Car Details: {self.year} {self.brand} {self.model}")

    def start(self):
        print(f"{self.brand} {self.model} is starting...")

car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Accord", 2022)

car1.display_details()
car1.start()

car2.display_details()
car2.start()

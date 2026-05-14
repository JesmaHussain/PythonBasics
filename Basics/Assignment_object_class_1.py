class Car:
    def __init__(self,brand, model):
        self.brand = brand
        self.model = model
    def display(self):
        print("The brand of the car:",self.brand,"\n","the model of the car:", self.model)
car1=Car("Ford", "Mustang")
car2=Car("Honda", "Honda City")
car1.display()
car2.display()
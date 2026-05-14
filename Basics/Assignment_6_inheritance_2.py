class Vehicle:#parent class
    def __init__(self,vehicle_name):
        self.vehicle_name=vehicle_name
        print("the vehicle name is :",self.vehicle_name)

class Bike(Vehicle):#child class
     def __init__(self,vehicle_name):
         super().__init__(vehicle_name)

object=Bike("Ducati")
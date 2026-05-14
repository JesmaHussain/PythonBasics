#parent class
class Company:
    def __init__(self,company_name):
        self.company_name=company_name

class Employee(Company):#child class
    def display(self):
        print("the company name of the employee:",self.company_name)

object=Employee("Ust")
object.display()



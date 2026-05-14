class Calc:
    def __int__(self,a,b):
        self.a=int(input("enter your first number:"))
        self.b=int(input("enter your second number:"))
    def add(self):
        print("the addition of two numbers=",self.a+self.b)
    def sub(self):
        print("the substraction of two numbers=",self.a-self.b)
#a=int(input("enter your first number:"))
#b=int(input("enter your second number:"))
cal=Calc()
cal.add()
cal.sub()


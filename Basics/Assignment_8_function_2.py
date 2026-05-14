def display():
    number=int(input("enter the number"))
    result=square(number)
    print("the square of the given number is ",result)

def square(number):
    return number*number

display()
def display():
    string = input("enter the string")
    length = len(string)
    print("the string in reverse order is :")
    for i in range(length):
        print(string[length - i - 1])
display()
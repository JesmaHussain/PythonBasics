while 1:
    print("\n","do you want to continue?")
    print("\n","press Y/N")
    press=input()
    if press=='Y':
        number=int(input("enter a number"))
    elif press!='Y' and press!='N':
        print("invalid input")
    else:
        break

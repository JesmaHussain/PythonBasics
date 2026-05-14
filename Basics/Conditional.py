"""age=int(input("enter the person age"))
if age>=18:
    print("the person is eligible to vote")
else:
    print("the person is not eligible to vote")"""

"""age=int(input("enter the person age"))
if (age<13):
    print("the person is Child")
elif (age>=13 and age<18):
    print("the person is Teenager")
else:
    print("the person is Adult")"""


x=int(input("enter the first number"))
y=int(input("enter the second number"))
choose=input("enter the choice")
if choose=='+':
    print(x+y)
elif choose=='-':
    print(x-y)
elif choose=='*':
    print(x*y)
elif choose=='/':
    print(x/y)
else:
    print("the choice is invalid")

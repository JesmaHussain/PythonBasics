list1=[]
count=int(input("limit of the numbers"))
print("enter the numbers")
for i in range(count):
    val=int(input())
    if val!=0:
        list1.append(val)
    else:
        print("zero is not accepted")
        break

print(list1)

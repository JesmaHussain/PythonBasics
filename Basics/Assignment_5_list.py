list1=[]
limit=int(input("Enter a number of limit of the list"))
for i in range(limit):
    value = input("Enter a number")

    list1.append(value)
print("the list of numbers :",list1)
print("the first element of the list:",list1[0])
print("the last elements in the list:",list1[-1])
list1.insert(3,"HI")
print("the new list:",list1)
print("the count of elements in the list:",len(list1))

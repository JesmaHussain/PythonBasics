"""name="alexander"
i=0
for i in name:
    if i=="x":
        continue
    print (i)"""
name=input("Enter your name:")
length=len(name)
i=0
while 1:
    if name[i]=='x':
        continue
        i=i+1
    print(name[i])



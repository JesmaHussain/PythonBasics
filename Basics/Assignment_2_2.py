string=input("enter the string")
new=""
message=""
count=0
count1=0
length=len(string)
for i in range(length):
        if string[i]=='a'or string[i]=='e'or string[i]=='i'or string[i]=='o'or string[i]=='u'or string[i]=='A'or string[i]=='E'or string[i]=='I'or string[i]=='O'or string[i]=='U':
            new=new+string[i]
            count = count + 1
        else:
            message=message+string[i]
            count1=count1+1

print("vowels present in string","=",new)
print("without vowels present in string","=",message)
print("the number of vowels=",count,"\n","the number of without vowels=",count1)


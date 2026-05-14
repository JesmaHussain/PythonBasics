def find_reverse(*args):
    list1=list(args)
    print(list1)
    length = len(list1)
    list1.reverse()
    print("the reverse of the given list is :",list1)
    print("the length of the given list is :",length)
find_reverse( 45,67,89,90,46,399)
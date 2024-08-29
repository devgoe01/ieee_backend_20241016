s1=input("enter string 1 ")
s2=input("enter string 2 ")
def listofstring (string):
    list=[]
    for i in string:
        list.append(i)
    return list
list1=listofstring(s1)
list2=listofstring(s2)
list_common=list(set(list1).intersection(list2))
if len(list_common) == 0:
    print("strings are complementary")
else:
    print("strings are not complementary")
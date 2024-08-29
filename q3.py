t=int(input("enter no. of items in list "))
list=[]
for m in range(1,t+1):
    element=int(input(f"enter the {m}th element: "))
    list.append(element)
target=int(input("enter the target "))
a=[]
for i in range(0,len(list)):
    for i in list:
        list.remove(i)
        for k in list:
            if k+i==target:
                a.append((i,k))
                list.remove(k)
print(a)
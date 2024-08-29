a=int(input("enter the 1st number "))
b=int(input("enter the 2nd number "))
c=int(input("enter the 3rd number "))
d=int(input("enter the 4th number "))
e=int(input("enter the 5th number "))
common_factors=[]

#not necessary to define a function
def cfactor_gen(num1,num2,num3,num4,num5):
    n=max(num1,num2,num3,num4,num5)
    for i in range(1,(n+2)//2):
        if num1%i==0 and num2%i==0 and num3%i==0 and num4%i==0 and num5%i==0:
            common_factors.append(i)
    return common_factors
print(f"entered digits are {a} , {b} , {c} , {d} , {e}")
print(f"highest common divisor is {max(cfactor_gen(a,b,c,d,e))})")
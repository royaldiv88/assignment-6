#fucntion to check number is perfect or not
a=int(input("enter any number"))
x=0
for i in range(1,a):
    if (a%i==0):
        x=x+i
if x==a:
    print("perfect number")
else:
    print("not a perfect number")

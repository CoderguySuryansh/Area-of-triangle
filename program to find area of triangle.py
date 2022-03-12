x=float(input("ENTER FIRST SIDE :" ))
y=float(input("ENTER SECOND SIDE :" ))
z=float(input("ENTER THIRD SIDE :" ))

s=(x+y+z)/2
print("semi permimeter will be :",s)
a=s-x
b=s-y
c=s-z
d=a*b*c
e=d*s
f=e**0.5
print("AREA OF TRIANGLE :",f)

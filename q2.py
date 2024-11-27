#write a code in python to use different type of operator
print("this program demonstrate operator")
a=int(input("enter the first number"))
b=int(input("enter the second number"))
r=input("enter the operator sign , which you want ot perform")
if r=="+" :
    print(f"sum of a+b is : {a+b}")
elif r=="-":
    print(f"the subtract of a-b is : {a-b}")  

else:
    print(f"you have choosen values that haven't been added to program")
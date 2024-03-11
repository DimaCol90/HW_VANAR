def ii(which):
    print(f"Enter {which} integer: ",end="")
    return int(input())

a=ii("first")
b=ii("second")

op=input("choose operation (* / + -): ")

if op in ["+","-","/","*"]:
    if op == "+":
        res=a+b
    elif op=="-":
        res=a-b
    elif op=="*":
        res=a*b
    elif op=="/":
        res=a/b
        
    print(f"result = {res}")
    
else:
    print("No such operation")



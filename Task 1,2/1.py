import mathM
op = str(input("Enter Operation? (/,*,-,+) "))
x = int(input("Enter the 1st NO. :"))
y = int(input("Enter the 2nd NO. :"))
if(op =='+'):
    print(mathM.sum(x,y))

elif(op=='-'):
    print(mathM.sub(x,y))

elif(op=='*'):
    print(mathM.mult(x,y))

elif(op=='/'):
    print(mathM.div(x,y))
else:
    print("ERR Insertion --> you allowed to insert /,*,-,+")
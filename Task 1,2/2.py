class employee:
    name=''
    age=0
    dept = ''
    phone = ''

emp = employee
emp.name = input("Name: ")
emp.age = int(input("Age: "))
emp.dept = input("Department: ")
emp.phone = input("Phone: ")

def empAge(age):
    if(18 < age < 30):
        print("The Employee is young")
    elif(age > 30):
        print("The Employee is Old")
    else:
        print("Illegal age")
        
empAge(emp.age)
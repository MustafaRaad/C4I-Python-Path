List=[]
while True:
    insertion = (input("Please enter your name: "))
    if (len(insertion) > 7):
        print('\"Name is more then 7 char\"')
        break
    List.append(insertion)
    print(List)
    if(insertion[0] == insertion[len(insertion)-1]):
        print('Good')
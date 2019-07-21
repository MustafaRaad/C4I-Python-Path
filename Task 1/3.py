class details():
    def __init__(self,name,age,title,salary,field):
       self.name = name
       self.age = age
       self.title = title
       self.salary = salary
       self.field = field
    def printer(self):
        print(self.name +' '+str(self.age) +' '+ self.title+' '+str(self.salary)+' '+self.field )
    pass
class manager(): 
    title = 'mr'
    salary = 120
    field = 'BIT'
    pass
class employee(manager,details): 
    manag=manager()
    det = details('mustafa',23,manag.title,manag.salary,manag.field)
    det.printer()
    pass

import trigers
class carInfo():
    def __init__(self,country,modelYear,color,fuelType):
        self.country = country
        self.modelYear = modelYear
        self.color = color
        self.fuelType = fuelType

class chasi(carInfo):
    def __init__(self,country,modelYear,color,fuelType, carType,vinNO):
        carInfo.__init__(self,country,modelYear,color,fuelType)
        self.carType = carType
        self.vinNO=vinNO

    def output(self):

        print(self.country,self.modelYear ,self.color,self.fuelType,self.carType,self.vinNO)
        trigers.model(self.modelYear)
        if(self.carType == 'Mercedes'):
            trigers.price('merc')
        else:
            trigers.price('!merc')
        trigers.cust(self.country,self.carType,self.modelYear)
            

o = chasi('Germany',2012,'red','Gazoline','Mercedes',1234)
o.output()
# o = chasi('USA',1997,'red','Gazoline','Cadellac',123456)
# o.output()
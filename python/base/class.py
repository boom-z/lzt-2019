class Calculator:
    name='Good calculator'
    price=18
    def __init__(self,name,price,hight,width,weight):
        self.name=name
        self.price=price
        self.hight=hight
        self.wi=width
        self.we=weight
        self.add(1,2)
    def add(self,x,y):
        print(self.name)
        result=x+y
        print(result)

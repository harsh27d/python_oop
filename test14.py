class vector:
    def __init__(self, x, y,x1,y2):
        self.x1=x1
        self.y2=y2
        self.x = x
        self.y = y

    def add(self):
       return self.x+self.y,self.x1+self.y2
obj1=vector(4,5,50,10)
obj1.add()
print(obj1.add())
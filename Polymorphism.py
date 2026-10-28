class Shape:
    def area():
        pass

class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def area(self):
        return self.length*self.breadth

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return 3.14*self.radius**2

shapes=[Rectangle(5,4),Circle(5)]
for shape in shapes:
    print(f"Area:{shape.area()}\n")


    

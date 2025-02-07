class Shape:
  def area(self):
      return 0

class Rectangle(Shape):
  def __init__(self, length, width):
      self.length = length  
      self.width = width  

  def area(self):
      return self.length * self.width


rectangle = Rectangle(4, 6)
print("Area of Rectangle:", rectangle.area()) 

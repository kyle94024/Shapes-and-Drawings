from geometricshape import GeometricShape

class Rectangle(GeometricShape):
  def __init__(self,stroke,fill,x,y,length,height):
    super(Rectangle,self).__init__(x,y,stroke,fill)
    self.height = height
    self.length = length
    print("rect length: ")
    print(length)
    print(self.length)

  
  def draw(self):
    super(Rectangle,self).draw()
    rect(super(Rectangle,self).getX(),super(Rectangle,self).getY(),self.length,self.height)

  def getHeight(self):
    return self.height

  def getLength(self):
    return self.length
  
  def dimensionSet(self,length,height):
    self.height = height
    self.length = length

  def dimensionAdd(self,length,height):
    self.height += height
    self.length += length


    

  
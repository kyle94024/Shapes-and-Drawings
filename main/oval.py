from geometricshape import GeometricShape

class Oval(GeometricShape):
  def __init__(self,stroke,fill,x,y,length,height):
    super(Oval,self).__init__(x,y,stroke,fill)
    self.height = height
    self.length = length
  
  def draw(self):
    super(Oval,self).draw()
    ellipse(super(Oval,self).getX(),super(Oval,self).getY(),self.length,self.height)

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


    

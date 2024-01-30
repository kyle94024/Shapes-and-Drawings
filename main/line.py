
from geometricshape import GeometricShape

class Line(GeometricShape):
  
  def __init__(self,stroke,x1,y1,x2,y2):
    super(Line,self).__init__(x1,y1,stroke,[0,0,0])
    self.stroke = stroke
    self.x2=x2
    self.y2=y2

  def draw(self):
    super().draw()
    line(super(Line,self).getX(),super(Line,self).getY(),self.x2,self.y2)

  def setFirst(self,x,y):
    super(Line,self).moveTo(x,y)

  def setSecond(self,x,y):
    self.x2 = x
    self.y2 = y

  def moveTo(self,x,y):
    self.x2 = self.x2 + x-self.x
    self.y2 = self.y2 + y-self.y
    self.x = x
    self.y = y

  def moveBy(self,x,y):
    self.x2 += x
    self.y2 += y
    self.x += x
    self.y += y
  
  def __str__(self):
    string = str(self.x2)+str(self.y2)
    
    return string

    
    


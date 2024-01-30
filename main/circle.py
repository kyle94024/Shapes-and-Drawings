from oval import Oval

class Circle(Oval):
  def __init__(self,stroke,fill,x,y,sideLength):
    super(Circle,self).__init__(stroke,fill,x,y,sideLength,sideLength)
    
  def dimensionSet(self,amount):
    super(Circle,self).dimensionSet(amount,amount)

  def dimensionAdd(self,amount):
    super(Circle,self).dimensionAdd(amount,amount)

  def draw(self):
    super(Circle,self).draw()

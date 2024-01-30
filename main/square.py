from rectangle import Rectangle

class Square(Rectangle):
  def __init__(self,stroke,fill,x,y,sideLength):
    super(Square,self).__init__(stroke,fill,x,y,sideLength,sideLength)
    
  def dimensionSet(self,amount):
    super(Square,self).dimensionSet(amount,amount)

  def dimensionAdd(self,amount):
    super(Square,self).dimensionAdd(amount,amount)

  def draw(self):
    super(Square,self).draw()








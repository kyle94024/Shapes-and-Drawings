from geometricshape import GeometricShape

class Polygon(GeometricShape):
  def __init__(self,stroke,fill,points):
    super(Polygon,self).__init__(0,0,stroke,fill)
    self.stroke = stroke
    self.fill = fill
    self.points = points

  def draw(self):
    super(Polygon,self).draw()
    poly = createShape()
    poly.beginShape()
    for i in self.points:
      poly.vertex(i[0],i[1])
    poly.endShape(CLOSE)
    shape(poly,0,0)

  def __str__(self):
    string = ""
    for i in self.points:
      string += str(i[0]) + "," + str(i[1]) + " "
    return string

  def moveBy(self,x,y):
    for point in range(0,len(self.points)):
      self.points[point] = (self.points[point][0]+x,self.points[point][1]+y)

  def moveTo(self,x,y):
    x = x-self.points[0][0]
    y = y-self.points[0][1]
    for point in range(0,len(self.points)):
      self.points[point] = (self.points[point][0]+x,self.points[point][1]+y)

      


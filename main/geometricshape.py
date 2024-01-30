class GeometricShape(object): 
  def __init__(self,x,y,s,f):
    self.x = x
    self.y = y
    self.rotation = 0
    self.strokeWeight = 1
    self.isVisible = True
    self.f = f
    self.s = s
    #print("fill: ")
    #print(f)
    #print("stroke: ")
    #print(s)
    #fill(self.f[0], self.f[1], self.f[2])
    #stroke(self.s[0], self.s[1], self.s[2])

  def __str__(self):
    return "x: " + str(self.x) + " y: " + str(self.y) + "isVisible: " + str(self.isVisible)

  def draw(self):
    fill(self.f[0],self.f[1],self.f[2])
    stroke(self.s[0],self.s[1],self.s[2])

  def moveBy(self,x,y):
    self.x += x
    self.y += y
  
  def moveTo(self,x,y):
    self.x = x
    self.y = y
  
  def getX(self):
    return self.x
  
  def getY(self):
    return self.y

  def hide(self):
    self.isVisible = False

  def show(self):
    self.isVisible = True
  
  def addRotate(self,amount):
    self.rotation += amount
  
  def setRotate(self,amount):
    self.rotation = amount

  def setFill(self,r,g,b):
    self.f = [r,g,b]
  
  def setStroke(self,r,g,b):
    self.s = [r,g,b]


  

  

  
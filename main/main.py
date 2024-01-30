from geometricshape import GeometricShape
from rectangle import Rectangle
from square import Square
from oval import Oval
from circle import Circle
from line import Line
from polygon import Polygon
import random
#from replit import audio
#source = audio.play_file("")


ledCounter = 0
#creating objs
ground = Rectangle([200,200,200],[240,240,240],0,307,900,450)
house = Polygon([0,0,0],[112,68,38],[(141+25,325+25),(141+25,222+25),(200+25,184+25),(256+25,222+25),(256+25,325+25)])
house3d1 = Polygon([0,0,0],[112,68,38],[(256+25,222+25),(256+25,325+25),(280+25,290+25),(280+25,190+25)])
house3d2 = Polygon([245,245,245],[245,245,245],[(200+25,184+25),(256+25,222+25),(280+25,190+25),(224+25,152+25)])
house3d3 = Polygon([245,245,245],[245,245,245],[(142+25,221+25),(200+25,184+25),(224+25,153+25),(165+25,195+25)])
tree1p1 = Polygon([33,107,34],[33,107,34],[(36+25,240+25),(70+25,190+25),(104+25,240+25)])
tree1p2 = Polygon([33,107,34],[33,107,34],[(36+25,260+25),(70+25,210+25),(104+25,260+25)])
tree1p3 = Polygon([33,107,34],[33,107,34],[(36+25,280+25),(70+25,230+25),(104+25,280+25)])
tree1p4 = Polygon([33,107,34],[33,107,34],[(36+25,300+25),(70+25,250+25),(104+25,300+25)])
tree1trunk = Rectangle([61, 34, 14],[61, 34, 14],82,316,25,50)
tree1snow = Polygon([230,230,230],[245,245,245],[(69+25,189+25),(52+25,215+25),(89+25,215+25)])
ornament1p1 = Circle([255,0,0],[230, 50, 30],84,255,10)
ornament1p2 = Circle([0,255,0],[10, 255, 10],102,267,10)
ornament1p3 = Circle([137, 207, 240],[137, 207, 240],88,287,10)
ornament1p4 = Circle([255,0,0],[230, 50, 30],103,299,10)
ornament1p5 = Circle([252, 219, 28],[252, 219, 28],82,314,10)
door = Rectangle([0,0,0],[186, 28, 4],233,291,32,59)
doorknob = Circle([0,0,0],[174, 180, 181],242,320,7)
window = Square([0,0,0],[212, 244, 252],186,299,30)
chim1 = Polygon([0,0,0],[112,68,38],[(260,215),(243,205),(243,188),(260,188)])
chim2 = Polygon([0,0,0],[112,68,38],[(260,215),(267,205),(267,178),(260,189)])
chim3 = Polygon([0,0,0],[112,68,38],[(267,177),(250,177),(250,188),(267,193)])
chim4 = Polygon([0,0,0],[112,68,38],[(250,178),(243,188),(243,193),(250,196)])

tree2p1 = Polygon([20, 94, 10],[20, 94, 10],[(312+25,240-30+25),(346+25,190-30+25),(380+25,240-30+25)])
tree2p2 = Polygon([20, 94, 10],[20, 94, 10],[(312+25,260-30+25),(346+25,210-30+25),(380+25,260-30+25)])
tree2p3 = Polygon([20, 94, 10],[20, 94, 10],[(312+25,280-30+25),(346+25,230-30+25),(380+25,280-30+25)])
tree2p4 = Polygon([20, 94, 10],[20, 94, 10],[(312+25,300-30+25),(346+25,250-30+25),(380+25,300-30+25)])
tree2trunk = Rectangle([61, 34, 14],[61, 34, 14],82+276,316-30,25,50)
tree2snow = Polygon([230,230,230],[250,250,250],[(354,209),(371,184),(389,209)])
ornament2p1 = Circle([137, 207, 240],[137, 207, 240],84+276,255-21,10)
ornament2p2 = Circle([252, 239, 40],[202, 219, 80],102+276,267-30,10)
ornament2p3 = Circle([255,0,0],[255,0,0],88+276,287-30,10)
ornament2p4 = Circle([0,255,0],[0,255,0],103+276,299-30,10)
ornament2p5 = Circle([137, 207, 240],[137, 207, 240],82+276,314-30,10)

tree3p1 = Polygon([20, 94, 10],[20, 94, 10],[(312+25+300,240-30+25+49),(346+25+300,190-30+25+49),(380+25+300,240-30+25+49)])
tree3p2 = Polygon([20, 94, 10],[20, 94, 10],[(312+25+300,260-30+25+49),(346+25+300,210-30+25+49),(380+25+300,260-30+25+49)])
tree3p3 = Polygon([20, 94, 10],[20, 94, 10],[(312+25+300,280-30+25+49),(346+25+300,230-30+25+49),(380+25+300,280-30+25+49)])
tree3p4 = Polygon([20, 94, 10],[20, 94, 10],[(312+25+300,300-30+25+49),(346+25+300,250-30+25+49),(380+25+300,300-30+25+49)])
tree3trunk = Rectangle([61, 34, 14],[61, 34, 14],82+276+300,316-30+49,25,50)
tree3snow = Polygon([230,230,230],[250,250,250],[(354+300,209+49),(371+300,184+49),(389+300,209+49)])
ornament3p2 = Circle([137, 207, 240],[137, 207, 240],102+276+303,267-30+40,10)
ornament3p3 = Circle([0,255,0],[0,255,0],88+276+310,287-30+40,10)
ornament3p4 = Circle([0,0,255],[0,0,255],103+276+280,299-30+40,10)
ornament3p5 = Circle([255,0,0],[255,0,0],82+276+320,314-30+45,10)

led1 = Oval([255,0,0],[255,0,0],176,245,5,10)
led2 = Oval([255,0,0],[255,0,0],200,231,5,10)
led3 = Oval([255,0,0],[255,0,0],225,215,5,10)
led4 = Oval([255,0,0],[255,0,0],247,229,5,10)
led5 = Oval([255,0,0],[255,0,0],271,245,5,10)
red = [led1,led2,led3,led4,led5]
led6 = Oval([0,255,0],[0,255,0],188,239,5,10)
led7 = Oval([0,255,0],[0,255,0],213,222,5,10)
led8 = Oval([0,255,0],[0,255,0],237,223,5,10)
led9 = Oval([0,255,0],[0,255,0],260,239,5,10)
green = [led6,led7,led8,led9]
icicle1 = Polygon([171, 248, 255],[171, 248, 255],[(153+25,216+25),(158+25,212+25),(156+25,238+25)])
icicle2 = Polygon([171, 248, 255],[171, 248, 255],[(175+25,202+25),(178+25,199+25),(176+25,215+25)])
icicle3 = Polygon([171, 248, 255],[171, 248, 255],[(231+25,203+25),(236+25,207+25),(234+25,226+25)])
snowmanbig = Circle([120,120,120],[240,240,240],467,362,50)
snowmanmid = Circle([120,120,120],[240,240,240],467,326,40)
snowmansmall = Circle([120,120,120],[240,240,240],467,296,30)
snowmanrarm = Polygon([150,150,150],[164,116,73],[(482,322),(504,319),(505,314),(498,316),(498,311),(495,313),(493,316),(481,319)])
snowmanlarm = Polygon([150,150,150],[164,116,73],[(934-482,322),(934-504,319),(934-505,314),(934-498,316),(934-498,311),(934-495,313),(934-493,316),(934-481,319)])
snowmanleye = Circle([0,0,0],[0,0,0],461,294,3)
snowmanreye = Circle([0,0,0],[0,0,0],470,294,3)
snowmanhat = Polygon([0,0,0],[0,0,0],[(452,286),(480,286),(480,282),(474, 282),(474, 260),(458, 260),(458, 282),(452, 282)])
snowmanbutton1 = Circle([0,0,0],[0,0,0],466,316,4)
snowmanbutton2 = Circle([0,0,0],[0,0,0],466,326,4)
snowmanbutton3 = Circle([0,0,0],[0,0,0],466,336,4)
snowmanbutton4 = Circle([0,0,0],[0,0,0],466,356,4)
snowmanbutton5 = Circle([0,0,0],[0,0,0],466,366,4)
snowmanbutton6 = Circle([0,0,0],[0,0,0],466,376,4)
snowmancarrot = Polygon([217,125,0],[237,145,3],[(465,297),(465,302),(446,300)])

tree4p1 = Polygon([33,107,34],[33,107,34],[(36+25+480,240+25-40),(70+25+480,190+25-40),(104+25+480,240+25-40)])
tree4p2 = Polygon([33,107,34],[33,107,34],[(36+25+480,260+25-40),(70+25+480,210+25-40),(104+25+480,260+25-40)])
tree4p3 = Polygon([33,107,34],[33,107,34],[(36+25+480,280+25-40),(70+25+480,230+25-40),(104+25+480,280+25-40)])
tree4p4 = Polygon([33,107,34],[33,107,34],[(36+25+480,300+25-40),(70+25+480,250+25-40),(104+25+480,300+25-40)])
tree4trunk = Rectangle([61, 34, 14],[61, 34, 14],82+480,316-40,25,50)
tree4snow = Polygon([230,230,230],[245,245,245],[(69+25+480,189+25-40),(52+25+480,215+25-40),(89+25+480,215+25-40)])
ornament4p1 = Circle([255,0,0],[230, 50, 30],84+480,255-40,10)
ornament4p2 = Circle([0,255,0],[10, 255, 10],102+480,267-40,10)
ornament4p3 = Circle([137, 207, 240],[137, 207, 240],88+480,287-40,10)
ornament4p4 = Circle([255,0,0],[230, 50, 30],103+480,299-40,10)
ornament4p5 = Circle([252, 219, 28],[252, 219, 28],82+480,314-40,10)



tree5p1 = Polygon([33,107,34],[33,107,34],[(36+25+600,240+25-33),(70+25+600,190+25-33),(104+25+600,240+25-33)])
tree5p2 = Polygon([33,107,34],[33,107,34],[(36+25+600,260+25-33),(70+25+600,210+25-33),(104+25+600,260+25-33)])
tree5p3 = Polygon([33,107,34],[33,107,34],[(36+25+600,280+25-33),(70+25+600,230+25-33),(104+25+600,280+25-33)])
tree5p4 = Polygon([33,107,34],[33,107,34],[(36+25+600,300+25-33),(70+25+600,250+25-33),(104+25+600,300+25-33)])
tree5trunk = Rectangle([61, 34, 14],[61, 34, 14],82+600,316-33,25,50)
tree5snow = Polygon([230,230,230],[245,245,245],[(69+25+600,189+25-33),(52+25+600,215+25-33),(89+25+600,215+25-33)])
ornament5p1 = Circle([255,0,0],[230, 50, 30],84+600,255-33,10)
ornament5p2 = Circle([0,255,0],[10, 255, 10],102+600,267-33,10)
ornament5p3 = Circle([137, 207, 240],[137, 207, 240],88+600,287-33,10)
ornament5p4 = Circle([255,0,0],[230, 50, 30],103+600,299-33,10)
ornament5p5 = Circle([252, 219, 28],[252, 219, 28],82+600,314-33,10)

tree6p1 = Polygon([33,107,34],[33,107,34],[(36+25-59,240+25-37),(70+25-59,190+25-37),(104+25-59,240+25-37)])
tree6p2 = Polygon([33,107,34],[33,107,34],[(36+25-59,260+25-37),(70+25-59,210+25-37),(104+25-59,260+25-37)])
tree6p3 = Polygon([33,107,34],[33,107,34],[(36+25-59,280+25-37),(70+25-59,230+25-37),(104+25-59,280+25-37)])
tree6p4 = Polygon([33,107,34],[33,107,34],[(36+25-59,300+25-37),(70+25-59,250+25-37),(104+25-59,300+25-37)])
tree6trunk = Rectangle([61, 34, 14],[61, 34, 14],82-59,316-37,25,50)
tree6snow = Polygon([230,230,230],[245,245,245],[(69+25-59,189+25-37),(52+25-59,215+25-37),(89+25-59,215+25-37)])
ornament6p1 = Circle([255,0,0],[230, 50, 30],84-59,255-37,10)
ornament6p2 = Circle([0,255,0],[10, 255, 10],102-59,267-37,10)
ornament6p3 = Circle([137, 207, 240],[137, 207, 240],88-59,287-37,10)
ornament6p4 = Circle([255,0,0],[230, 50, 30],103-59,299-37,10)
ornament6p5 = Circle([252, 219, 28],[252, 219, 28],82-59,314-37,10)

smoke = []

  
snow = []
for i in range(0,300):
  snow.append(Circle([255,255,255],[255,255,255],random.randint(0,1000),random.randint(-405,-5),5))

snow2 = []
for i in range(0,300):
  snow2.append(Circle([255,255,255],[255,255,255],random.randint(0,1000),random.randint(-405,-5),5))

def setup():
  size(850,420)

def draw():
  global ledCounter
  global smoke
  smoke = list(filter(None,smoke))
  ledCounter += 1
  if ledCounter == 50:
    for i in red:
      i.setFill(0,255,0)
      i.setStroke(0,255,0)
    for i in green:
      i.setFill(255,0,0)
      i.setStroke(255,0,0)
  if ledCounter == 100:
    for i in red:
      i.setFill(255,0,0)
      i.setStroke(255,0,0)
    for i in green:
      i.setFill(0,255,0)
      i.setStroke(0,255,0)
    ledCounter = 0
  background(0, 234, 255)
  

  # drawing
  ground.draw()
  house.draw()
  house3d1.draw()
  house3d2.draw()
  house3d3.draw()

  tree6trunk.draw()
  tree6p4.draw()
  tree6p3.draw()
  tree6p2.draw()
  tree6p1.draw()
  tree6snow.draw()
  ornament6p1.draw()
  ornament6p2.draw()
  ornament6p3.draw()
  ornament6p4.draw()
  ornament6p5.draw()

  tree1trunk.draw()
  tree1p4.draw()
  tree1p3.draw()
  tree1p2.draw()
  tree1p1.draw()
  tree1snow.draw()
  ornament1p1.draw()
  ornament1p2.draw()
  ornament1p3.draw()
  ornament1p4.draw()
  ornament1p5.draw()
  door.draw()
  doorknob.draw()
  window.draw()
  tree2trunk.draw()
  tree2p4.draw()
  tree2p3.draw()
  tree2p2.draw()
  tree2p1.draw()
  tree2snow.draw()
  ornament2p1.draw()
  ornament2p2.draw()
  ornament2p3.draw()
  ornament2p4.draw()
  ornament2p5.draw()
  tree4trunk.draw()
  tree4p4.draw()
  tree4p3.draw()
  tree4p2.draw()
  tree4p1.draw()
  tree4snow.draw()
  ornament4p1.draw()
  ornament4p2.draw()
  ornament4p3.draw()
  ornament4p4.draw()
  ornament4p5.draw()
  tree5trunk.draw()
  tree5p4.draw()
  tree5p3.draw()
  tree5p2.draw()
  tree5p1.draw()
  tree5snow.draw()
  ornament5p1.draw()
  ornament5p2.draw()
  ornament5p3.draw()
  ornament5p4.draw()
  ornament5p5.draw()
  tree3trunk.draw()
  tree3p4.draw()
  tree3p3.draw()
  tree3p2.draw()
  tree3p1.draw()
  tree3snow.draw()
  ornament3p2.draw()
  ornament3p3.draw()
  ornament3p4.draw()
  ornament3p5.draw()
  
  led1.draw()
  led2.draw()
  led3.draw()
  led4.draw()
  led5.draw()
  led6.draw()
  led7.draw()
  led8.draw()
  led9.draw()
  icicle1.draw()
  icicle2.draw()
  icicle3.draw()
  snowmanbig.draw()
  snowmanmid.draw()
  snowmansmall.draw()
  snowmanrarm.draw()
  snowmanlarm.draw()
  snowmanleye.draw()
  snowmanreye.draw()
  snowmanhat.draw()
  snowmanbutton1.draw()
  snowmanbutton2.draw()
  snowmanbutton3.draw()
  snowmanbutton4.draw()
  snowmanbutton5.draw()
  snowmanbutton6.draw()
  snowmancarrot.draw()
  chim3.draw()
  chim4.draw()
  
  sg = random.randint(0,15)
  if sg == 0:
    sc = random.randint(150,200)
    smoke.append(Circle([sc,sc,sc],[sc,sc,sc],253,188,random.randint(5,30)))
  
  for i in range(len(smoke)):
    smoke[i].moveTo(smoke[i].getX()+0.1,smoke[i].getY()-0.6)
    smoke[i].dimensionAdd(0.1)
    smoke[i].draw()
    if smoke[i].getY() < -10:
      smoke[i] = None

      
  chim1.draw()
  chim2.draw()
  

  #window 
  #green-red switching LEDs
  #snowman 
  # snow angels/steps
  #pavement in front of house
  #snow on tree and house roof
  #chimney & smoke
  #sun/clouds (probably not)
  #wind (very very hard)
  #glowing tree star
  #presents under tree (but thats strange because outdoors)
  




  for i in range(len(snow)):
    snow[i].moveTo(snow[i].getX()-0.5,snow[i].getY()+1)
    snow[i].draw()
    if snow[i].getY() > 455:
      snow[i].moveTo(random.randint(0,1000),-5)

  for i in range(len(snow2)):
    snow2[i].moveTo(snow2[i].getX()-0.1,snow2[i].getY()+0.8)
    snow2[i].draw()
    if snow2[i].getY() > 455:
      snow2[i].moveTo(random.randint(0,1000),-5)
  
  
def mouseClicked():
  print(str(mouseX) + " " + str(mouseY))
  

'''



rectangle1 = Rectangle([200,200,200],[240,240,240],0,307,400,400)

#testing:
print(rectangle1)

print(circle1)
print(oval1)
print(square1)
print(line1)
'''
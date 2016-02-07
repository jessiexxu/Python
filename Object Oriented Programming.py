# Problem 1 Create class methods to accept coordinate as a pair of 
# tuples and return the slope and distance of the line.

import math
class Line(object):
    
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    
    def distance(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return math.sqrt((x2-x1)**2+(y2-y1)**2)
    
    def slope(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return (y2-y1)/float(x2-x1)

# EXAMPLE OUTPUT
coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)
li.distance()
li.slope()

# Problem 2 Create class methods to calculate volume and surface area of a cylinder.

class Cylinder(object):
    
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
        
    def volume(self):
        return round(math.pi*self.radius**2*self.height,1)
    
    def surface_area(self):
        top = math.pi*self.radius**2
        return round(2*top + 2*math.pi*self.radius*self.height,1)

# EXAMPLE OUTPUT
c = Cylinder(2,3)
c.volume()
c.surface_area()

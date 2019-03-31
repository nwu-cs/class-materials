import numpy as np

class Point:

    def __init__(self,xc=0,yc=0):
        self.x = xc
        self.y = yc

    def __add__(self, other):
        result = Point()
        result.x = self.x + other.x
        result.y = self.y + other.y
        return result

    def __str__(self):
        return "(%d,%d)" % (self.x,self.y)
    
class Circle:
    
    def __init__(self,p=None,r=0):
        if p is None:
            self.origin = Point()
        else:
             self.origin = Point(p.x,p.y)
        self.radius = r
        
    def get_area(self):
        return self.radius * self.radius * 3.14158
    
    def moveto(self,p:Point):
        self.origin = p
        
    def moveby(self,p:Point):
        np = self.origin + p
        self.origin = np
    
class Rectangle:
    
    def __init__(self,p=None,w=0,h=0):
        if p is None:
            self.origin = Point()
        else:
             self.origin = Point(p.x,p.y)
        self.width = w
        self.height = h
        
    def get_area(self):
        return self.width * self.height
    
    def moveto(self,p:Point):
        self.origin = p
        
    def moveby(self,p:Point):
        np = self.origin + p
        self.origin = np
    
def point_in_circle(p,c):    
    n = (((p.x-c.origin.x)**2)+((p.y-c.origin.y)**2))**.5
    if n <= c.radius:
        return True
    else:
        return False
    
def rectangle_in_circle(r,c):
    c1= Point(r.origin.x + .5 * r.width,r.origin.y + .5 * r.height)
    c2= Point(r.origin.x + .5 * r.width,r.origin.y - .5 * r.height)
    c3= Point(r.origin.x - .5 * r.width,r.origin.y + .5 * r.height)
    c4= Point(r.origin.x - .5 * r.width,r.origin.y - .5 * r.height)
    n1= point_in_circle(c1,c)
    n2= point_in_circle(c2,c)
    n3= point_in_circle(c3,c)
    n4= point_in_circle(c4,c)
    if n1 and n2 and n3 and n4 == True:
        return True
    else:
        return False

def fiverandomcircles():
    l = []
    for i in range(5):
        r = np.random.randint(5,50)
        c = Circle(Point(150,100),r)
        l.append(c)
    return l
        


if  __name__ == "__main__":     
    t = fiverandomcircles()
    i = 0
    for f in t:        
        print("circle %d : center (%d,%d), radius %d" % (i, f.origin.x, f.origin.y, f.radius))
        i += 1
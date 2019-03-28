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


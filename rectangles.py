'''Python function that calculates the area and perimeter of a rectangle'''
from math import *
class point: ''' A class point is a Python tuple object of (Xcord,Ycord) of real numbers as prompted therefore this first class function initializes the point'''
    def __init__(self,Xcord, Ycord):
        self.Xcord= Xcord
        Self.Ycord= Ycord
    def getXcord(self): '''The getXcord function is an accessor method that encapsulates the data (gets data)'''
        return self.Xcord
    def getYcord(self):
        return self.Ycord
class rectangle: '''An instance of class point '''
    def __init__(self,bottonLeftCorner,topRightcorner): '''A bottonleft corner and topright corner are initialized as instances of the class rectangle'''
        self.bottonLeftCorner= bottonLeftCorner
        self.topRightCorner= topRightCorner
        self.RectLen=self.getRectLen(self.bottonLeftCorner.getXcord(),self.topRightCorner.getXcord())
        self.RectWidth=self.getRectWidth(self.bottonLeftCorner.getYcord(),self.topRightCorner.getYcord())
    def getbottonLeftCorner(self):
        return self.bottonLeftCorner
    def gettopRightcorner(self):
        return self.topRightCorner
    def getbottonRightCorner(self):
        return Point(self.gettopRightCorner.getXcord(),self.getbottonLeftCorner.getYcord())
    def gettopleftcorner(self):
        return Point(self.gettopRightCorner.getYcord(),self.getbottonLeftCorner.getXcord())
    def getRectLen(self,Xaxis,Yaxis):
        Length=math.sqrt((Xaxis**2)+(Yaxis**2))
    def Area(self): '''Area class that calculates the area of a given point rectangle'''
        return self.RectLen*self.RectWidth
    def perimeter(self): '''Area class that calculates the perimeter of a given point rectangle'''
        return 2*(self.RectLen+self.RectWidth)
    
    def intersects(RectangleA, RectangleB):'''this function checks if rectangles intersect or not'''
        topRightcornerA=RectangleA.gettopRightcorner()
        topRightcornerB=RectangleB.gettopRightcorner()
        topLeftcornerA=RectangleA.gettopLeftcorner()
        topLeftcornerB=RectangleB.gettopLeftcorner()
        bottonLeftCornerA=RectangleA.getbottonLeftCorner()
        bottonLeftCornerB=RectangleB.getbottonLeftCorner()
        bottonRightCornerA=RectangleA.getbottonRightCorner()
        c=RectangleB.getbottonRightCorner()
        
        
       '''Now using Rectangle A as base Rectangle on which all other rectangles must intersect if true'''
    ArrayIntersectA=[False,False,False,False] '''this line of code already assigned a non intersect as false in order to make all other conditions true per the diagram'''
    for every Rectangle in Intersects:
        if PointIn(topRightcornerB,RectangleA):
            ArrayIntersectA[0]=True
        if PointIn(topLeftcornerB,RectangleA):
            ArrayIntersectA[1]=True
        if PointIn( bottonRightCornerB,RecatangleA):
            ArrayIntersectA[2]=True
        if PointIn(topLeftcornerB,RectangleA):
            ArrayIntersectA[3]=True
        if ArrayIntersectA.count(True)>0 and < 3:
            print (True)
            
            
       
          
            
        
        
        
        
        
        
        
    
    
  
    

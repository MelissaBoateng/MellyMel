from math import *
class point:
    def __init__(self,Xcord, Ycord):
        self.Xcord= Xcord
        Self.Ycord= Ycord
    def getXcord(self):
        return self.Xcord
    def getYcord(self):
        return self.Ycord
class rectangle:
    def __init__(self,bottonLeftCorner,topRightcorner):
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
    def Area(self):
        return self.RectLen*self.RectWidth
    def perimeter(self):
        return 2*(self.RectLen+self.RectWidth)
        
        
        
        
    
    
  
    
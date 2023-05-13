import numpy as np

class tile:
    
    def __init__(self,x,y,s):
        self.pos = np.array([x,y])
        self.sorte = s #1=neutral building block, 2,3,4,5 x+,x-,y+,y-
        self.updateFlag = 0
        
        
    
    def getXY(self):
        return self.pos
        
    def move(self,dx,dy):
        self.pos+=np.array([dx,dy])
        
    def setUpdateFlag(self,f):
        self.updateFlag = f
        
    def getUpdateFlag(self):
        return self.updateFlag
        
        
    
        
    def getSorte(self):
        return self.sorte
        
    
        
     
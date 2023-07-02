import tile
import numpy as np

class world:

    def __init__(self):
        print("init world")
        self.tileList = []
        
    def reset(self):
        print("Reset World")
        self.tileList = []
        
    def getTiles(self):
        return self.tileList
        
    def setTiles(self,t):
        self.tileList = t
        
    def addTile(self,x,y,s):
        self.tileList.append(tile.tile(x,y,s))
        
    def getNeighbours(self,t):
        nList = []
        for n in self.tileList:
            #print(np.linalg.norm(t.getXY()-n.getXY()))
            if np.linalg.norm(t.getXY()-n.getXY()) == 1.0:
                nList.append(n)
        
        #print(nList)
        return nList
        
    def getNeighbourIdL(self,t):
        idList = []
        for i in range(len(self.tileList)):
            #print(np.linalg.norm(t.getXY()-n.getXY()))
            if np.linalg.norm(t.getXY()-n.getXY()) == 1.0:
                nList.append(n)
        
        #print(nList)
        return nList
        
        
    def updateMove(self):
        #print("-----\n")
        #print(self.tileList)
         
        
        for t in range(len(self.tileList)):
            #print("Update Flag: ", [i.getUpdateFlag() for i in self.tileList])
            nodes = []
            if self.tileList[t].getSorte() >= 2 and self.tileList[t].getSorte() <= 5 and self.tileList[t].getUpdateFlag()==0:
                
                nodes.append(self.tileList[t])
                self.tileList[t].setUpdateFlag(1)
                #print("Starting nodes: ",nodes)
                for depth in range(100):
                    searchdone = True
                    #print("Search Iteration ",depth, " nodes: ", nodes)
                    for n in range(len(nodes)):
                        neighbours = self.getNeighbours(nodes[n])
                        
                            
                        for n in neighbours:
                            if n.getUpdateFlag() == 0 and n.getSorte()==1:
                                searchdone = False
                                n.setUpdateFlag(1)
                                nodes.append(n)
                    if searchdone :
                        #print("Cancelled Search")
                        break
                
            
        

        
            for n in nodes:
                if self.tileList[t].getSorte() == 2:
                    n.move(1,0)
                if self.tileList[t].getSorte() == 3:
                    n.move(-1,0)
                if self.tileList[t].getSorte() == 4:
                    n.move(0,1)
                if self.tileList[t].getSorte() == 5:
                    n.move(0,-1)    
                  
            
        
        
            for t in self.tileList:
                t.setUpdateFlag(0)
        
        
        
        
        
        
        
    def update(self):
        self.updateMove()
           
        
        
        
    
        
        
    

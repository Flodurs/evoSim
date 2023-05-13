import world
import numpy as np
import random

class genAlg: #maybe but this in seperate thread
    def __init__(self):
        random.seed()
        print("Init Genetic")
        self.w = world.world()
        self.buildingArea = [20,20,4,4] #Rect x,y,len x,len y
        self.genePool = []
        self.geneNum = 5
        self.geneLen = self.buildingArea[2]*self.buildingArea[3]
        self.fitness = [0 for i in range(self.geneNum)]
        
        
    def seedGenes(self):
        for x in range(self.geneNum):
            self.genePool.append([1 for i in range(self.geneLen)])
            
    def getWorld(self):
        return self.w
    
    def runSimUpdate(self):
        self.w.update()
    
    def placeGeneInWorld(self,world,gene):
        print("Place Gene in World")
        #print(self.genePool[gene])
        for a in range(self.geneLen):
            #print(self.buildingArea[0]+(a%self.buildingArea[2]),int(self.buildingArea[1]+(a/self.buildingArea[3])))
            world.addTile(self.buildingArea[0]+a%self.buildingArea[2],int(self.buildingArea[1]+a/self.buildingArea[3]),self.genePool[gene][a])
            
    def calcFitness(self, tileList): #tileList represents worldstate after simulation aka 100 steps 
        print("Calculating Fitness")
        fit = 0
        for t in tileList:
            if t.getXY()[0] > 50:
                fit+=1
        return fit
                
                
            
    def getCurrentTopPeformTileList(self):
        print("returning current top performing Gene")
        w = world.world()
        self.placeGeneInWorld(w,self.fitness.index(max(self.fitness)))
        #print(w.getTiles())
        return w.getTiles()
        
        
    def simulateGeneration(self): 
        #Simulate each Gene
        for g in range(self.geneNum):
            self.w.reset()
            self.placeGeneInWorld(self.w,g)
            
            print("Start Simulating")
            
            for step in range(100):
                self.w.update()
                print("Gene: ", g , "Step: ", step)
                
            self.fitness[g]=self.calcFitness(self.w.getTiles())

        #locate best performing gene (or top n genes)
        bestGene = self.genePool[self.fitness.index(max(self.fitness))]
        print("Top Fitness: ", max(self.fitness), "Gene Id: ", self.fitness.index(max(self.fitness)), "Gene: ", bestGene)
        
        self.genePool[self.geneNum-1] = bestGene.copy()
        
        
            
        #mutate them and fill genePool again
        for g in range(self.geneNum-1):
            self.genePool[g]=bestGene
            
        for g in range(self.geneNum-1):
            self.genePool[g][random.randint(0,self.geneLen-1)]=random.randint(1,5)
        
        print(self.genePool)
            
            
        
        
        
        
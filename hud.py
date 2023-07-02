import button

class hud:
    def __init__(self):
        self.buttonList = []
        self.buttonList.append(button.button(0,0,100,35,"Evolve",self.toggleSimulatingOn))
        
        
        self.simulating = False
        
    def update(self,screen):
        for b in self.buttonList:
            b.update(screen)
            
    def toggleSimulatingOn(self):
        self.simulating = True
        print("Toggle")
        
    def getSimulating(self):
        if self.simulating == True:
            self.simulating = False
            return True
        return False
        
        
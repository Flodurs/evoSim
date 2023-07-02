import button

class hud:
    def __init__(self):
        self.buttonList = []
        self.buttonList.append(button.button(0,0,100,35,"Evolve",self.toggleSimulating))
        
        
        self.simulating = False
        
    def update(self,screen):
        for b in self.buttonList:
            b.update(screen)
            
    def toggleSimulating(self):
        self.simulating = True
        
    def getSimulating(self):
        return self.simulating
        
        
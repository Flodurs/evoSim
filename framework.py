import pygame
import world
import genAlg


class framework:

    def __init__(self):
        
        self.zoomLevel = 1.0
        self.sim = genAlg.genAlg()
        self.sim.seedGenes()
        #self.sim.placeGeneInWorld(1)
        self.w = world.world()
        
        
    def getColorFromSorte(self,s):
        if s == 1:
            return [100,200,100]
        if s == 2:
            return [200,100,100]
            
        return [255,255,255]


    def renderTiles(self,screen):
        for t in self.w.getTiles():
            pygame.draw.rect(screen,self.getColorFromSorte(t.getSorte()), pygame.Rect(t.getXY()[0]*10*self.zoomLevel,t.getXY()[1]*10*self.zoomLevel,10*self.zoomLevel, 10*self.zoomLevel))
            
        

     
    def run(self):
        pygame.init()
        
        screen = pygame.display.set_mode([1000, 600])
        
        
        running = True

        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_g: 
                        self.sim.simulateGeneration()
                        self.w.reset()
                        self.w.setTiles(self.sim.getCurrentTopPeformTileList().copy())
                    if event.key == pygame.K_u: 
                        self.w.update()
                        
                        
                        
                    if event.key == pygame.K_ESCAPE: 
                        running = False
                
            
            
            #retrieve current top performing gene from Simulation Thread           
            #display top performing Gene while the Simulation runs along in 2nd thread  
            
            screen.fill((0,0,0))
            self.renderTiles(screen)


           

            pygame.display.flip()

        pygame.quit()
    
    


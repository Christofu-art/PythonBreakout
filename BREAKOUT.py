import pygame
import random
pygame.init()

screen = pygame.display.set_mode((700,500))
pygame.display.set_caption("breakout")

#variables to hold paddle position
bx = 350 #xposition
by = 250 #yposition
bVx = 5 #x velocity (horizontal speed)
bVy = 5 #y velocity (vertical speed)
#these go above game loop
p1x = 300
p1y = 480
p1Score = 0
doExit = False

class brick:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.color = (random.randrange(100, 250),random.randrange(100, 250),random.randrange(100, 250))
        self.isDead = False
    def draw(self):
        pygame.draw.rect(screen, self.color, (self.xpos, self.ypos, 100, 50))
    #bounding box collision
    def collide(self, ball_x, ball_y):
        if not self.isDead:
            if (ball_x + ball_size > self.xpos and
                ball_x < self.xpos + 100 and  # Width of brick is 100
                ball_y + ball_size > self.ypos and
                ball_y < self.ypos + 50):    # Height of brick is 50
                self.isDead = True
                return True
        return False

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()
b1 = brick(50, 50) #these go ABOVE yuor game loop
b2 = brick(50, 100)
b3 = brick(150, 50)
b4 = brick(150, 100)
b5 = brick(250, 50)
b6 = brick(250, 100)
b7 = brick(350, 50)
b8 = brick(350, 100)
b9 = brick(450, 50)
b10 = brick(450, 100)
b11 = brick(550, 50)
b12 = brick(550, 100)
while not doExit: #GAME LOOP###############################################################################################
    #event queue stuff
    clock.tick(60)
    
    for event in pygame.event.get(): #check if user did somethign
        if event.type == pygame.QUIT: #check if user clicked close
            doExit = True #Flag that we are done so we exit game loop
            
 
    #game logic will go here-------------------------------------
    bx += bVx
    by += bVy

    #reflect ball off side walls of screen
    if bx < 0: #hit left side 
        bVx *= -1
        p1Score += 1
        
    if bx + 100 > 700: #hit right side
        bVx *= -1
        
    if by < 0 or by + 20 > 500:
        bVy *= -1
       
        
        
        #ball-paddle relfection
    if bx < p1x + 50 and by + 20 > p1y and by < p1y + 100:
        bVx *= -1

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        p1x-=5
    if keys[pygame.K_d]:
        p1x+=5
        
        
        
        #render section will go here---------------------------------
    screen.fill((0,0,0))
    b1.draw() #these go IN your render section, inside the game loop
    b2.draw()
    b3.draw()
    b4.draw()
    b5.draw()
    b6.draw()
    b7.draw()
    b8.draw()
    b9.draw()
    b10.draw()
    b11.draw()
    b12.draw()
    #display scores
    font = pygame.font.Font(None, 74) #use default font
    text = font.render(str(p1Score), 1, (255, 255, 255))
    screen.blit(text, (20,10))
        #draw a rectangle
    pygame.draw.rect(screen, (255, 255, 255), (p1x, p1y, 100, 20), 1)
    pygame.draw.circle(screen, (255, 255, 255), (bx, by), 25)
        #update the screen
    pygame.display.flip()
pygame.quit()
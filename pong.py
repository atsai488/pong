import pygame
pygame.init()
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Test run')

BLACK = (0, 0, 0)

FPS = 30

bouncy = pygame.Rect(350, 350, 15, 15)
other_rect = pygame.Rect(WIDTH/2 - 50, 100, 20, 100)
bXSpeed, bYSpeed = 6, 7

def handleCollision(other_rect, bouncy, collsionTolerance):
    global bXSpeed, bYSpeed
    if (bouncy.colliderect(other_rect)):
        if abs(other_rect.top - bouncy.bottom) <= collsionTolerance and bYSpeed > 0:
            bYSpeed *= -1
        elif abs(other_rect.bottom - bouncy.top) <= collsionTolerance and bYSpeed < 0:
            bYSpeed *= -1
        elif abs(other_rect.right - bouncy.left) <= collsionTolerance and bXSpeed > 0 and bouncy.x > WIDTH/2:
            bXSpeed *= -1
        elif abs(other_rect.left - bouncy.right) <= collsionTolerance and bXSpeed < 0 and bouncy.x < WIDTH/2:
            bXSpeed *= -1

def rectMovement():
    keys_pressed = pygame.key.get_pressed()
    VEL = 10
    if keys_pressed[pygame.K_LEFT] and other_rect.x - VEL > 0: #left
            other_rect.x -= VEL        
    if keys_pressed[pygame.K_RIGHT] and other_rect.x + other_rect.width + VEL - 20 < WIDTH:
        other_rect.x += VEL  
    if keys_pressed[pygame.K_UP]: #up
        other_rect.y -= VEL        
    if keys_pressed[pygame.K_DOWN]: #down
        other_rect.y += VEL
def ballInBound():
    global bXSpeed, bYSpeed
    if (bouncy.right >= WIDTH):
        bXSpeed *= -1
        bXSpeed *= 1.01
    if (bouncy.bottom >= HEIGHT or bouncy.top <= 0):
        bYSpeed *= -1
        bYSpeed *= 1.01
def bounceRect(bouncy):
    global bXSpeed, bYSpeed
    WIN.fill(BLACK)
    bouncy.x += bXSpeed
    bouncy.y += bYSpeed
    
    ballInBound()
        
    rectMovement()
        
        
    collsionTolerance = 50
    
    handleCollision(other_rect, bouncy, collsionTolerance)
    
    
    pygame.draw.rect(WIN, (255, 0, 0), other_rect)
    pygame.draw.rect(WIN, (255, 255, 255), bouncy)
    pygame.display.update()
    



def main():

    
    clock = pygame.time.Clock()
    run = True
    
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        bounceRect(bouncy)   
    pygame.quit()      
    
if __name__ == "__main__":
    main()      
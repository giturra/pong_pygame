import pygame, sys

pygame.init()


class Player:

    def __init__(self):
        self.rect = pygame.rect.Rect((64, 64, 16, 16))
    
    def handle_keys(self):
        key = pygame.key.get_pressed()
        dist = 1
        if key[pygame.K_LEFT]:
            self.rect.move_ip(-1, 0)
        if self.rect.x < 0:
            self.rect.x = 0
        if key[pygame.K_RIGHT]:
            self.rect.move_ip(1, 0)
        if self.rect.x > 300 - 16:
            self.rect.x = 300 - 16
        if key[pygame.K_UP]:
            self.rect.move_ip(0, -1)
        if self.rect.y < 0:
            self.rect.y = 0
        if key[pygame.K_DOWN]:
            self.rect.move_ip(0, 1)
        if self.rect.y > 400 - 16:
            self.rect.y = 400 - 16
    def draw(self, surface):
        pygame.draw.rect(surface, (0, 0, 128), self.rect)
    

screen = pygame.display.set_mode((300, 400))
pygame.display.set_caption("Medio Poto")

running = True

pink = (255, 192, 203)

player = Player()

while running:

    

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
            break
    
    screen.fill((255, 255, 255))

    player.draw(screen)
    player.handle_keys()
    pygame.display.update()
    

pygame.quit()

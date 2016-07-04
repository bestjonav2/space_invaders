import pygame

class Disparo(pygame.sprite.Sprite):
    def __init__(self, posx, posy, ruta, personaje):
        pygame.sprite.Sprite.__init__(self)
        self.imagenBala = pygame.image.load(ruta)
        self.rect = self.imagenBala.get_rect()
        self.velDisparo = 5
        self.rect.top = posy
        self.rect.left = posx
        self.disparoPj = personaje

    def trayectoria(self):
        if self.disparoPj == True:
            self.rect.top = self.rect.top - self.velDisparo
        else:
            self.rect.top = self.rect.top + self.velDisparo
    def dibujar(self, superficie):
        superficie.blit(self.imagenBala, self.rect)

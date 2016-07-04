import pygame
import Disparo


class NaveEspacial(pygame.sprite.Sprite):

    def __init__(self, ancho, alto):
        pygame.sprite.Sprite.__init__(self)
        self.imagenNave = pygame.image.load("imgs/alien.png")
        #self.imgExplo1 = pygame.image.load("imgs/explosion1.png")
        self.imgExplo2 = pygame.image.load("imgs/explosion2.png")
        #self.imgExplo3 = pygame.image.load("imgs/explosion3.png")
        self.rect = self.imagenNave.get_rect()
        self.rect.centerx = ancho/2
        self.rect.centery = alto-30
        self.sonidoDisparo = pygame.mixer.Sound("sounds/shot.wav")
        self.sonidoExplosion = pygame.mixer.Sound("sounds/explosion.wav")
        self.listaDisparo = []
        #self.listaExplosiones = [self.imagenNave,self.imgExplo1,self.imgExplo2,self.imgExplo3]
        #self.tiempoCambio = 1
        #self.indexExplo = 0
        #self.imgExplo = self.listaExplosiones[self.indexExplo]
        self.vida = True
        self.velocidad = 20
    def movIzq(self):
        self.rect.left -= self.velocidad
        self.__mov()
    def movDer(self):
        self.rect.right += self.velocidad
        self.__mov()
    def __mov(self):
        if self.vida == True:
            if self.rect.left <= 0:
                self.rect.left = 0
            elif self.rect.right>900:
                self.rect.right = 900
    def destroy(self):
        self.sonidoExplosion.play()
        self.vida == False
        self.velocidad = 0
        #self.imgExplo = self.listaExplosiones[self.indexExplo]
        self.imagenNave = self.imgExplo2
        # if self.tiempoCambio == tiempo:
        #     print self.indexExplo
        #     self.indexExplo += 1
        #     self.tiempoCambio += 1
        #     if self.indexExplo > len(self.listaExplosiones)-1:
        #         self.indexExplo = 3
    def disparar(self,x,y):
        miBala = Disparo.Disparo(x,y,"imgs/bala.png",True)
        self.listaDisparo.append(miBala)
        self.sonidoDisparo.play()
    def dibujar(self, superficie):
        superficie.blit(self.imagenNave, self.rect)

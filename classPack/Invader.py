import pygame
from random import randint
import Disparo

class Invader(pygame.sprite.Sprite):
    def __init__(self, posx, posy, distance, imgagenUno, imagenDos):
        pygame.sprite.Sprite.__init__(self)
        self.imagenInv1 = pygame.image.load(imgagenUno)
        self.imagenInv2 = pygame.image.load(imagenDos)
        self.listaInvaders = [self.imagenInv1, self.imagenInv2]
        self.indexInvader = 0
        self.imagenInvader = self.listaInvaders[self.indexInvader]
        self.rect = self.imagenInvader.get_rect()
        #atributos de disparo
        self.rangoDisparo = 1
        self.tiempoCambio = 1
        self.sonidoDisparo = pygame.mixer.Sound("sounds/enemyshot.wav")
        self.listaDisparo = []
        #posicion inicial
        self.rect.top = posy
        self.rect.left = posx
        self.stopEnemy = False
        #atributos de mov
        self.varDes = .5
        self.velocidad = 10.0*self.varDes
        self.derecha = True
        self.contador = 0
        self.contadorDes = 1.0
        self.maxDescenso = self.rect.top + 40
        self.limiteDer = posx+distance
        self.limiteIzq = posx-distance
    def cambio(self, tiempo):
        if self.stopEnemy == False:
            self.__movInvader()
            self.__atack()
            if self.tiempoCambio == tiempo:
                self.indexInvader += 1
                self.tiempoCambio += 1
                if self.indexInvader > len(self.listaInvaders) -1:
                    self.indexInvader = 0
    def __movInvader(self):
        if self.contador < 3: #real value is 3
            self.__movLateral()
        else:
            self.__descenso()
    def __descenso(self):
        if self.maxDescenso == self.rect.top:
            self.contador=0
            #Aumenta velocidad de el invader cada que baja.
            # if self.velocidad < 15:
            #     self.varDes = self.contadorDes/4
            #     self.velocidad = 10.0 * self.varDes
            #     self.contadorDes += 1.0
            if self.rect.top <= 450:
                self.maxDescenso = self.rect.top + 40
        else:
            self.rect.top +=1
    def __movLateral(self):
        if self.derecha == True:
            self.rect.left = self.rect.left + self.velocidad
            if self.rect.left > self.limiteDer:
                self.derecha = False
                self.contador += 1
        else:
            self.rect.left = self.rect.left - self.velocidad
            if self.rect.left < self.limiteIzq:
                self.derecha = True

    def dibujar(self, superficie):
        superficie.blit(self.imagenInvader, self.rect)
        self.imagenInvader = self.listaInvaders[self.indexInvader]
    def __atack(self):
        if (randint(0,100)<self.rangoDisparo):
            self.__disparar()
    def __disparar(self):
        x,y = self.rect.center
        balaEnem = Disparo.Disparo(x,y,"imgs/balaEnemy.png", False)
        self.listaDisparo.append(balaEnem)
        self.sonidoDisparo.play()

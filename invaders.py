import pygame, sys, os
from pygame.locals import *
from classPack import NaveEspacial
from classPack import Invader
from time import time
#globalvars
ancho = 900
alto = 480
listaEnemigo = []
def reset():
     python = sys.executable
     os.execl(python, python, * sys.argv)
def loadEnemy():
    posx = 100
    for x in range(1,5):
        enemy = Invader(posx, 100, 100,"imgs/invaderG.png","imgs/invaderR.png")
        listaEnemigo.append(enemy)
        posx += 200
    posx = 100
    for x in range(1,5):
        enemy = Invader(posx, 0, 100,"imgs/invaderG.png","imgs/invaderR.png")
        listaEnemigo.append(enemy)
        posx += 200
    posx = 100
    for x in range(1,5):
        enemy = Invader(posx, -100, 100,"imgs/invaderG.png","imgs/invaderR.png")
        listaEnemigo.append(enemy)
        posx += 200

def SpaceInvader():
    pygame.init()
    ventana = pygame.display.set_mode((ancho,alto))
    pygame.display.set_caption("Ventana principal")
    fondo = pygame.image.load("imgs/Fondo.jpg")

    pygame.mixer.music.load("sounds/never8bit.wav")
    pygame.mixer.music.play(5)
    pygame.mixer.music.set_volume(.8)


    jugador = NaveEspacial(ancho, alto)
    loadEnemy()
    jugando = True
    fps = pygame.time.Clock()
    #------ Anuncios in-game
    imgGameOver = pygame.image.load("imgs/gameover.png")
    imgPause = pygame.image.load("imgs/pause.png")
    imgWin = pygame.image.load("imgs/win.png")
    isPaused = False
    winerino = False
    #destroyJug = False
    #contadorEx = 0
    while True:
        #jugador.mov() old method xdxdx
        fps.tick(60)
        tiempo = pygame.time.get_ticks()/1000
        time1 = time()
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
            if jugando == True:
                if evento.type == KEYDOWN:
                    if evento.key == K_LEFT:
                        jugador.movIzq()
                    elif evento.key == K_RIGHT:
                        jugador.movDer()
                    elif evento.key == K_z:
                        x,y = jugador.rect.center
                        jugador.disparar(x,y)
                    elif evento.key == K_p:
                        isPaused = True
                        ventana.blit(imgPause,(0,0))
                        pygame.display.flip()
                        while isPaused:
                            evento = pygame.event.wait()
                            if evento.type == QUIT:
                                pygame.quit()
                                sys.exit()
                            if evento.type == KEYDOWN:
                                if evento.key == K_p:
                                    break

        ventana.blit(fondo, (0,0))
        jugador.dibujar(ventana)

        if len(jugador.listaDisparo)>0:
            for x in jugador.listaDisparo:
                x.dibujar(ventana)
                x.trayectoria()

                if x.rect.top < -10:
                    jugador.listaDisparo.remove(x)
                else:
                    for enemy in listaEnemigo:
                        if x.rect.colliderect(enemy.rect):
                            listaEnemigo.remove(enemy)
                            jugador.listaDisparo.remove(x)
        if len(listaEnemigo)>0:
            for enemy in listaEnemigo:
                enemy.cambio(tiempo)
                enemy.dibujar(ventana)
                if enemy.rect.colliderect(jugador.rect):
                    jugando = False
                    jugador.destroy()
                    stopGame()

                if len(enemy.listaDisparo)>0:
                    for x in enemy.listaDisparo:
                        x.dibujar(ventana)
                        x.trayectoria()
                        if x.rect.colliderect(jugador.rect):
                            jugando = False
                            jugador.destroy()
                            stopGame()
                        if x.rect.top > 900:
                            enemy.listaDisparo.remove(x)
                        else:
                            for disp in jugador.listaDisparo:
                                if x.rect.colliderect(disp.rect):
                                    jugador.listaDisparo.remove(disp)
                                    enemy.listaDisparo.remove(x)
        else:
            jugando = False
            winerino = True

        # if destroyJug == True:
        #     while contadorEx < 3:
        #         jugador.destroy(contadorEx)
        #         pygame.time.delay(1000)
        #         contadorEx += 1
        #     jugando = False
        #     # while jugando:
        #     #
        #     #     print time2
        #     #     if time2 < 3:
        #     #         jugador.destroy(time2)
        #     #     else:
        #     #         jugando = False



        if jugando == False:
            pygame.mixer.music.fadeout(3000)
            if winerino == True:
                ventana.blit(imgWin,(0,0))
            else:
                ventana.blit(imgGameOver,(0,0))
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reset()
        pygame.display.update()

def stopGame():
    for enemigo in listaEnemigo:
        for disp in enemigo.listaDisparo:
            enemigo.listaDisparo.remove(disp)
        enemigo.stopEnemy = True

SpaceInvader()

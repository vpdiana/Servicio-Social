#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Se importa la paquetería a usar
import time
import pygame
from pygame.locals import *
from sys import exit
from pyfirmata import Arduino, SERVO
#Se especifican parametros de pyfirmata
board = Arduino('/dev/cu.usbmodem14101')
#Se define el pin 9 para el servomotor
board.digital[9].mode = SERVO
pygame.init()
#Se especifica el tamaño de la pantalla de pygame
screen = pygame.display.set_mode((460, 300))
#Se inicia el bucle de pygame
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    screen.lock()
    #posicion del rectangulo izquierdo dado el tamaño
    rectangle_pos = (60, 35)
    #posición del rectangulo derecho
    rectangle_pos2 = (280, 35)
    #tamaño de ambos rectángulos
    rectangle_size = (150, 250)
    #indicación de poner la pantalla en color negro (con su clave RGB)
    screen.fill((0,0,0))
    #dibujar los dos rectangulos en blanco (con clave RGB)
    r1 = pygame.draw.rect(screen, (255, 255, 255), Rect(rectangle_pos, rectangle_size,))
    r2 = pygame.draw.rect(screen, (255, 255, 255), Rect(rectangle_pos2, rectangle_size))
    #se señala el evento de dar clic con el mouse, o toque en la pantalla touch
    if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            #funcion que evalua si se presiona el rectangulo
            aa=r1.collidepoint(x, y)
            bb=r2.collidepoint(x,y)
            print(aa,bb)
            if (aa,bb) == (1,0):
                #si se presiona el rectangulo hacer sonar el buzzer
                board.digital[13].write(1)
                #esta corriente se manda un segundo
                time.sleep(0.25)
                #y despues se apaga
                board.digital[13].write(0)
                #al tiempo que el motor va a 0
                board.digital[9].write(0)
                time.sleep(1)
                board.digital[9].write(90)
            elif (aa,bb) == (0,1):
                board.digital[13].write(1)
                time.sleep(0.25)
                board.digital[13].write(0)
                time.sleep(1)
                board.digital[9].write(0)
                time.sleep(1)
                board.digital[9].write(90)
            else:
                board.digital[13].write(0)
                board.digital[9].write(90)
    screen.unlock()
    pygame.display.update()



import sys
import time
import json
import math
import random
import pygame
import socket
import pickle
import select
import copy
import tkinter as tk
from tkinter import messagebox
from snake import snake, cube, randomSnack, redrawWindow

def main():
    HOST = '127.0.0.1'  # retirado de exemplos feitos em sala
    PORT = 65432  # retirado de exemplos feitos em sala

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        width = 500
        rows = 20
        
        cobra = snake((255, 0, 200), (10, 10))  # criando snake do cliente
        s.connect((HOST, PORT))
        s.sendall(pickle.dumps(cobra))  # enviando dados da snake do cliente pro servidor
        data = s.recv(1024)  # recebendo dados do servidor
        my_snake = pickle.loads(data)  # recebendo as outras snakes do servidor

        s.sendall(pickle.dumps(cobra))   
        data = s.recv(1024)  
        snakes = pickle.loads(data)

        win = pygame.display.set_mode((width, width))
        flag = True 
        clock = pygame.time.Clock()
        t = time.clock()
        movimento = None

        while flag:
            pygame.time.delay(50)
            clock.tick(10)

            if movimento != None:
                s.sendall(pickle.dumps(movimento))
                movimento = None
            else:
                s.sendall(pickle.dumps(snakes))  

            data = s.recv(4096)  # recebendo dados do servidor
            
            if data:
                snakes = pickle.loads(data)  
            else:
                time.sleep(5)
                continue

            for event in pygame.event.get(): # verificando movimentos
                keys = pygame.key.get_pressed()
                for key in keys:
                    if keys[pygame.K_LEFT]:
                        movimento = 'left'

                    elif keys[pygame.K_RIGHT]:
                        movimento = 'right'

                    elif keys[pygame.K_UP]:
                        movimento = 'up'

                    elif keys[pygame.K_DOWN]:
                        movimento = 'down'

            snacks = snakes.pop('snacks')          
            redrawWindow(win, rows, width, snakes, snacks)
        pass

main()
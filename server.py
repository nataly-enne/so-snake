import sys
import time
import math
import random
import pygame
import socket, pickle
import select
import threading
import tkinter as tk
from tkinter import messagebox
from snake import snake, cube, randomSnack, redrawWindow

# testar se a cobra comeu alguma das frutas
def eat_snack(snack, snacks, snakes):
    threading.currentThread()
    global width, rows

    for j in snakes:
        if j != 'snacks':
            if snakes[j].body != [] and snakes[j].body[0].pos == snack.pos:
                snakes[j].addCube()
                snacks.remove(snack)
                snacks.append(cube(randomSnack(rows, snakes), color=(0, 255, 0)))
                break

def start_server():
    port = 65432
    read_list = []
    
    global width, rows
    width = 500
    rows = 20
    
    snakes = {} 
    snacks = [] 
    snacks.append(cube(randomSnack(rows, snakes), color=(0, 255, 0)))
    snakes['snacks'] = snacks

    clock = pygame.time.Clock()
    t = time.clock()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        
        pygame.time.delay(50) # definido pelo jogo original
        clock.tick(10) # definido pelo jogo original
        s.setblocking(0)
        s.bind(('', port))
        s.listen(5)
        read_list.append(s)

        while True:
            readable, writeable, error = select.select(read_list,[],[])

            for sock in readable:
                if sock is s: 
                    conn, addr = sock.accept()
                    read_list.append(conn)
                    data = conn.recv(4096)
                    snake_client = pickle.loads(data) #recebe snake do socket
                    snakes[addr] = snake_client
                    conn.send(pickle.dumps(addr))
                else:
                    data = sock.recv(4096)
                    
                    if data:
                        # recebendo movimentos do client
                        m = pickle.loads(data)
                        if type(m) == str: 
                            snakes[sock.getpeername()].move(m)

                        # Adicionando um snack a cada 0.5s
                        if (time.clock() - t) > 0.5:  
                            snacks.append(cube(randomSnack(rows, snakes), color=(0, 255, 0)))
                            snakes['snacks'] = snacks
                            t = time.clock()  

                        threads = []
                        for snack in snacks:
                            threads.append([])
                            threads[-1] = threading.Thread(target=eat_snack, args=(snack, snacks, snakes))
                            threads[-1].start() 
                        threads[-1].join()
                        threads.clear()

                        # movimentando as snakes
                        for i in snakes:
                            if i != 'snacks':
                                snakes[i].move()
                        sock.send(pickle.dumps(snakes))
                    else:
                        sock.close()
                        read_list.remove(sock)
            

start_server()
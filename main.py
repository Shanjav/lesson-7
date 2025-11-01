import pgzrun
from random import randint
from time import time

WIDTH = 800
HEIGHT = 600

satellites = []
num_of_satellites = 8
next_satellite = 0

lines = []

start_time = 0
end_time = 0
total_time = 0

def create_satellite():
    global start_time
    for i in range(0, num_of_satellites):
        satellite = Actor("satellite")
        satellite.pos = randint(50, 750), randint(50, 550)
        satellites.append(satellite)
    start_time = time()

def draw():
    screen.blit("space", (0,0))
    global total_time
    num = 1
    for satellite in satellites:
        satellite.draw()
        screen.draw.text(str(num), (satellite.pos[0], satellite.pos[1]+20))
        num = num+1
    for line in lines:
        screen.draw.line(line[0], line[1], (255,255,255))
    if next_satellite<num_of_satellites:
        total_time = time() - start_time
        screen.draw.text(str(total_time), (10,10))
    else:
        screen.draw.text(str(total_time), (10,10))

def update():
    pass
create_satellite()
pgzrun.go()
from body import Body
from simulation import Simulation
from vector import Vector2D
from renderer import Renderer
import pygame
import threading
import time
import numpy as np

def main():
    render = Renderer(800, 800, 50)
    simulation = Simulation()

    while render.running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                render.running = False

        simulation.update()

        render.draw_bodies(simulation.get_bodies())
        

        render.clock.tick(60)
    
    pygame.quit()

if __name__ == "__main__":
    main()


from body import Body
from simulation import Simulation
from vector import Vector2D
from renderer import Renderer
import pygame
import threading
import time
import numpy as np

def main():
    render = Renderer(800, 800)
    simulation = Simulation()



    while render.running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                render.running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    pygame.display.toggle_fullscreen()
            
            if event.type == pygame.MOUSEBUTTONDOWN:    
                if event.button == 1:  # Left click
                    render.dragging = True
                    render.prev_mouse_pos = pygame.mouse.get_pos()

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    render.dragging = False
        
        render.control_update()

        

        simulation.update()

        render.draw_bodies(simulation.get_bodies())

        render.clock.tick(60)
    
    pygame.quit()

if __name__ == "__main__":
    main()


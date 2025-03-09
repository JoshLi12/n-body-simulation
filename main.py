from body import Body
from simulation import Simulation
from vector import Vector2D
from renderer import Renderer
import pygame
import threading
import time
import numpy as np

MAX_UPDATES_PER_FRAME = 5
FIXED_DT = 1 / 60


def main():
    render = Renderer(800, 800)
    simulation = Simulation()

    last_time = time.time()
    accumulated_time = 0.0

    while render.running:
        current_time = time.time()
        frame_time = current_time - last_time
        last_time = current_time        

        accumulated_time += frame_time

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

        updates_this_frame = 0
        while accumulated_time >= FIXED_DT and updates_this_frame < MAX_UPDATES_PER_FRAME:
            simulation.update()  # Update simulation with a fixed time step
            accumulated_time -= FIXED_DT
            updates_this_frame += 1

        # simulation.update()
        alpha = accumulated_time / FIXED_DT

        render.draw_bodies(alpha, simulation.get_bodies())

        # render.clock.tick(60)
    
    pygame.quit()

if __name__ == "__main__":
    main()


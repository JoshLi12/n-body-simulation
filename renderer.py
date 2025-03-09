import pygame
import numpy as np
import math

class Renderer:
    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)
        pygame.display.set_caption("N-Body Simulation")
        self.clock = pygame.time.Clock()
        self.running = True
        self.font = pygame.font.Font(None, 20)
        self.offset_x, self.offset_y = 0, 0  # Panning offsets
        self.dragging = False
        self.prev_mouse_pos = (0, 0)
        self.target_offset_x, self.target_offset_y = 0, 0
        self.pan_speed = 0.5
        self.zoom = 10.0



    def draw_bodies(self, bodies):
        self.screen.fill((0,0,0))

        for body in bodies:
            pygame.draw.circle(
                self.screen,
                (255, 255, 255),
                (body.pos.x + self.offset_x, body.pos.y + self.offset_y),
                body.r # size
            )
        pygame.display.flip()
    
    def control_update(self):
        self.offset_x = self.interp(self.offset_x, self.target_offset_x, self.pan_speed)
        self.offset_y = self.interp(self.offset_y, self.target_offset_y, self.pan_speed)

        if self.dragging:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            dx, dy = mouse_x - self.prev_mouse_pos[0], mouse_y - self.prev_mouse_pos[1]
            self.target_offset_x += dx
            self.target_offset_y += dy
            self.prev_mouse_pos = (mouse_x, mouse_y)
    
    def interp(self, a, b, t):
        return a + (b-a) * t

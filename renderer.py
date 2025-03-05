import pygame
import numpy as np
import math

class Renderer:
    def __init__(self, width, height, grid_spacing):
        pygame.init()
        self.width = width
        self.height = height
        self.grid_spacing = grid_spacing
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("2-Body Simulation")
        self.clock = pygame.time.Clock()
        self.running = True
        self.font = pygame.font.Font(None, 20)
    
    def draw_grid(self):
        self.screen.fill((0, 0, 0))  # Background color (Black)
        grid_color = (50, 50, 50)  # Dark gray for grid lines
        text_color = (200, 200, 200)  # Light gray for labels

        origin_x = self.width // 2
        origin_y = self.height // 2

        # Draw vertical grid lines & labels
        for x in range(0, self.width, self.grid_spacing):
            pygame.draw.line(self.screen, grid_color, (x, 0), (x, self.height))

            # Only mark every second grid line to avoid clutter
            if x % (self.grid_spacing * 2) == 0:
                pixel_x = x - origin_x
                text = self.font.render(str(pixel_x), True, text_color)
                self.screen.blit(text, (x + 5, origin_y + 5))

        # Draw horizontal grid lines & labels
        for y in range(0, self.height, self.grid_spacing):
            pygame.draw.line(self.screen, grid_color, (0, y), (self.width, y))

            if y % (self.grid_spacing * 2) == 0:
                pixel_y = origin_y - y  # Flip Y-axis so up is positive
                text = self.font.render(str(pixel_y), True, text_color)
                self.screen.blit(text, (origin_x + 5, y - 10))

        # Draw XY axis (centered at middle of screen)
        pygame.draw.line(self.screen, (255, 255, 255), (origin_x, 0), (origin_x, self.height), 2)  # Y-axis
        pygame.draw.line(self.screen, (255, 255, 255), (0, origin_y), (self.width, origin_y), 2)  # X-axis

    def draw_bodies(self, bodies):
        self.screen.fill((0,0,0))

        for body in bodies:
            pygame.draw.circle(
                self.screen,
                (255, 255, 255),
                (body.pos.x, body.pos.y),
                body.r # size
            )
        pygame.display.flip()
    
    def run(self, bodies):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.draw_bodies(bodies)

            self.clock.tick(60)  # FPS = 60

        pygame.quit()
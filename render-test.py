import pygame
import numpy as np
import math

# Pygame setup
WIDTH, HEIGHT = 800, 600
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Sphere parameters
radius = 100
resolution = 20  # Number of latitudinal & longitudinal points
spheres = []

# Generate sphere function
def generate_sphere(center_x):
    vertices = []
    triangles = []
    
    for i in range(resolution + 1):
        theta = i * math.pi / resolution  # Latitude
        for j in range(resolution):
            phi = j * 2 * math.pi / resolution  # Longitude
            x = center_x + radius * math.sin(theta) * math.cos(phi)
            y = radius * math.sin(theta) * math.sin(phi)
            z = radius * math.cos(theta)
            vertices.append([x, y, z])

    for i in range(resolution):
        for j in range(resolution):
            p1 = i * resolution + j
            p2 = p1 + resolution
            p3 = (p1 + 1) % resolution + (i * resolution)
            p4 = (p2 + 1) % resolution + ((i + 1) * resolution)

            if i < resolution - 1:
                triangles.append([p1, p2, p3])
                triangles.append([p2, p4, p3])
    
    return vertices, triangles

# Create two spheres at different positions
spheres.append(generate_sphere(-150))  # Left sphere
spheres.append(generate_sphere(150))   # Right sphere

# Camera angles
yaw, pitch = 0, 0  # Rotation angles
mouse_sensitivity = 0.005
mouse_dragging = False
last_mouse_x, last_mouse_y = 0, 0

# Function to rotate a point
def rotate_point(point, yaw, pitch):
    x, y, z = point
    new_x = x * math.cos(yaw) - z * math.sin(yaw)
    new_z = x * math.sin(yaw) + z * math.cos(yaw)
    new_y = y * math.cos(pitch) - new_z * math.sin(pitch)
    new_z = y * math.sin(pitch) + new_z * math.cos(pitch)
    return [new_x, new_y, new_z]

# Function to project 3D points to 2D
distance = 500
def project_3d_to_2d(point):
    factor = distance / (distance + point[2])  # Perspective projection
    x = int(WIDTH / 2 + point[0] * factor)
    y = int(HEIGHT / 2 - point[1] * factor)
    return (x, y)

# Generate a 3D grid for the XZ plane
grid_lines = []
grid_size = 400
grid_spacing = 50

for i in range(-grid_size, grid_size + grid_spacing, grid_spacing):
    # Lines parallel to the Z-axis (X varies, Z constant)
    grid_lines.append(([-grid_size, 0, i], [grid_size, 0, i]))
    # Lines parallel to the X-axis (Z varies, X constant)
    grid_lines.append(([i, 0, -grid_size], [i, 0, grid_size]))

# XYZ Axis Lines
axis_lines = [
    ([-grid_size, 0, 0], [grid_size, 0, 0], (255, 0, 0)),  # X-axis (Red)
    ([0, -grid_size, 0], [0, grid_size, 0], (0, 255, 0)),  # Y-axis (Green)
    ([0, 0, -grid_size], [0, 0, grid_size], (0, 0, 255)),  # Z-axis (Blue)
]

running = True

while running:
    screen.fill((0, 0, 0))  # Background remains black, grid is drawn over it
    scroll_sensitivity = 50  # How fast zooming happens
    min_distance = 500  # Closest zoom limit
    max_distance = 10000  # Farthest zoom limit

    for event in pygame.event.get():
        print(distance)
        if event.type == pygame.QUIT:
            running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            distance = max(min_distance, min(max_distance, distance - 100))
        elif keys[pygame.K_DOWN]:
            distance += 100
            distance = max(min_distance, min(max_distance, distance + 100))

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                mouse_dragging = True
                last_mouse_x, last_mouse_y = event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                mouse_dragging = False
        elif event.type == pygame.MOUSEMOTION and mouse_dragging:
            dx, dy = event.pos[0] - last_mouse_x, event.pos[1] - last_mouse_y
            yaw += dx * mouse_sensitivity
            pitch -= dy * mouse_sensitivity
            pitch = max(-math.pi/2, min(math.pi/2, pitch))
            last_mouse_x, last_mouse_y = event.pos

    # Draw the grid
    for start, end in grid_lines:
        p1 = project_3d_to_2d(rotate_point(start, yaw, pitch))
        p2 = project_3d_to_2d(rotate_point(end, yaw, pitch))
        pygame.draw.line(screen, (50, 50, 50), p1, p2, 1)  # Gray grid lines

    # Draw XYZ axes
    for start, end, color in axis_lines:
        p1 = project_3d_to_2d(rotate_point(start, yaw, pitch))
        p2 = project_3d_to_2d(rotate_point(end, yaw, pitch))
        pygame.draw.line(screen, color, p1, p2, 2)  # Colored axis lines

    # Draw both spheres
    for vertices, triangles in spheres:
        transformed_vertices = [rotate_point(v, yaw, pitch) for v in vertices]
        projected_vertices = [project_3d_to_2d(v) for v in transformed_vertices]

        for tri in triangles:
            points = [projected_vertices[i] for i in tri]
            pygame.draw.polygon(screen, (255, 255, 255), points, 0)  # Solid white spheres

    pygame.display.flip()
    clock.tick(60)  # Limit FPS to 60

pygame.quit()

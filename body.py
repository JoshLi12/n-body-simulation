import numpy as np
from vector import Vector2D

class Body():
    def __init__(self, position: Vector2D, velocity: Vector2D, mass: float):
        self.pos = position
        self.vel = velocity
        self.acc = Vector2D(0.0, 0.0)
        self.mass = mass
    
    def update(self, dt):
        self.pos += self.vel * dt
        self.vel += self.acc * dt
        self.acc = Vector2D(0.0, 0.0)

    def get_pos(self):
        return self.pos
    
    def get_vel(self):
        return self.vel
    
    def get_acc(self):
        return self.acc

    def repr(self):
        return f"Body(pos={self.pos}, vel={self.vel}, mass={self.mass})"


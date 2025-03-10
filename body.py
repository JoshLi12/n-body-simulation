import numpy as np
from vector import Vector2D

class Body():
    def __init__(self, position: Vector2D, velocity: Vector2D, mass: float, r: int):
        self.pos = position
        self.prev_pos = position
        self.vel = velocity
        self.acc = Vector2D(0.0, 0.0)
        self.mass = mass
        self.r = r
    
    def update(self, dt):
        self.prev_pos = self.pos
        self.pos += self.vel * 0.5 * dt
        self.vel += self.acc * dt
        self.acc = Vector2D(0,0)
    
    def frame_interpolate(body, alpha):
        return body.prev_pos * (1 - alpha) + body.pos * alpha

    def get_pos(self):
        return self.pos
    
    def get_vel(self):
        return self.vel
    
    def get_acc(self):
        return self.acc

    def repr(self):
        return f"Body(pos={self.pos}, vel={self.vel}, mass={self.mass})"


import numpy as np
from body import Body
from vector import Vector2D


class Simulation():
    def __init__(self):
        self.dt = 0.000001
        self.bodies = []
        self.bodies.append(Body(Vector2D(0.5, 0.8), Vector2D(-0.3, 0.5), 5.0))
        self.bodies.append(Body(Vector2D(-0.5, -0.8), Vector2D(1.0, 0.7), 5.0))
    
    def update(self):
        r1 = self.bodies[0].get_pos()
        r2 = self.bodies[1].get_pos()

        m1 = self.bodies[0].mass
        m2 = self.bodies[1].mass

        r = r1 - r2
        r_mag = r.magnitude()
        tmp = r / (r_mag ** 3)

        self.bodies[0].acc += tmp * m2
        self.bodies[1].acc += tmp * m1
    
    def __repr__(self):
        return f"""
        Body 1 - Position: {self.bodies[0].pos}, Velocity: {self.bodies[0].vel}, Acceleration: {self.bodies[0].acc}, Mass: {self.bodies[0].mass}\n
        Body 2 - Position: {self.bodies[1].pos}, Velocity: {self.bodies[1].vel}, Acceleration: {self.bodies[1].acc}, Mass: {self.bodies[1].mass}
        
        """
        
    


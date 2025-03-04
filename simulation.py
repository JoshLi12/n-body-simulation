import numpy as np
from body import Body
from vector import Vector2D
import math


dt = 0.0001

class Simulation():
    def __init__(self):
        self.bodies = []
        self.bodies.append(Body(Vector2D((100)+500, -1*(100)+400), Vector2D(-7000,0), 10000.0))
        self.bodies.append(Body(Vector2D((-100)+500, -1*(-100)+400), Vector2D(7000, 0), 10000.0))
    
    def update(self):
        r1 = self.bodies[0].get_pos()
        r2 = self.bodies[1].get_pos()

        m1 = self.bodies[0].mass
        m2 = self.bodies[1].mass

        r = r1 - r2
        r_mag = r.magnitude()
        print(r_mag)

        tmp = r.normalize() / max((0.0001 * r_mag)**2, 1)
        tmp *= 500

        self.bodies[0].acc -= tmp * m2
        self.bodies[1].acc += tmp * m1
        # print("Acc 1", self.bodies[0].acc)
        # print("Acc 2", self.bodies[1].acc)

        self.bodies[0].update(dt)
        self.bodies[1].update(dt)

        print(self.bodies[0].vel)
    
    def __repr__(self):
        return f"""
        Body 1 - Position: {self.bodies[0].pos}, Velocity: {self.bodies[0].vel}, Acceleration: {self.bodies[0].acc}, Mass: {self.bodies[0].mass}\n
        Body 2 - Position: {self.bodies[1].pos}, Velocity: {self.bodies[1].vel}, Acceleration: {self.bodies[1].acc}, Mass: {self.bodies[1].mass}
        """
    def get_bodies(self):
        return self.bodies
    


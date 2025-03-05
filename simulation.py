import numpy as np
from body import Body
from vector import Vector2D
import math
import random


dt = 0.1
radius = 0.5
N = 100
v = 1.0
m = 1.0

class Simulation():
    def __init__(self):
        self.bodies = []

        for i in range(N):
            pos = Vector2D(random.randint(0, 800), random.randint(0, 800))
            vel = Vector2D(random.randint(-1, 1), random.randint(-1, 1))
            self.bodies.append(Body(pos, vel, m, radius))

        com_vol = sum((b.vel * b.mass for b in self.bodies), Vector2D(0,0))/N
        com_pos = sum((b.pos * b.mass for b in self.bodies), Vector2D(0,0))/N

        normalize_r = max(b.pos.magnitude() for b in self.bodies)

        for b in self.bodies:
            b.pos /= normalize_r
            


    
    def update(self):
        for i in range(N):
            for j in range(i+1, N):
                r1 = self.bodies[i].get_pos()
                r2 = self.bodies[j].get_pos()

                m1 = self.bodies[i].mass
                m2 = self.bodies[j].mass


                r = r2 - r1
                r_sq = r.x * r.x + r.y * r.y

                # if (r_sq <= 2 * radius * radius):
                #     return Vector2D(0, 0)

                tmp = (m1 * m2 / (r_sq + 0.1))
                force = r.normalize() * tmp

                self.bodies[i].acc -= force / m2
                self.bodies[j].acc += force / m1

        for i in range(N):
            self.bodies[i].update(dt)
            

        # print("Sum", self.bodies[0].vel + self.bodies[1].vel)

    
    def __repr__(self):
        return f"""
        Body 1 - Position: {self.bodies[0].pos}, Velocity: {self.bodies[0].vel}, Acceleration: {self.bodies[0].acc}, Mass: {self.bodies[0].mass}\n
        Body 2 - Position: {self.bodies[1].pos}, Velocity: {self.bodies[1].vel}, Acceleration: {self.bodies[1].acc}, Mass: {self.bodies[1].mass}
        """
    def get_bodies(self):
        return self.bodies
    


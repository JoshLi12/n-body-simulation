import numpy as np
from body import Body
from vector import Vector2D
import math
import random


dt = 0.1
radius = 1
N = 170
v = 1.0
m = 1.0
G = 10
sd = 150

class Simulation():
    def __init__(self):
        self.bodies = []

        def rand_pos():
            theta = random.uniform(0, 2 * math.pi)
            scale = (random.uniform(0, 1) ** 0.5) * sd
            return Vector2D(400 + math.cos(theta) * scale, 400 + math.sin(theta) * scale)
        
        def rand_vel():
            theta = random.uniform(0, 2 * math.pi)
            return Vector2D(math.cos(theta) * 5, math.sin(theta) * 5)


        for i in range(N):
            pos = rand_pos()
            vel = rand_vel()
            self.bodies.append(Body(pos, vel, m, radius))

        com_vel = sum((b.vel * b.mass for b in self.bodies), Vector2D(0,0))/N
        com_pos = sum((b.pos * b.mass for b in self.bodies), Vector2D(0,0))/N

        for b in self.bodies:
            b.vel -= com_vel
            b.pos -= com_pos
            b.pos += Vector2D(400, 400)

        normalize_r = max(b.pos.magnitude() for b in self.bodies)

        # for b in self.bodies:
        #     b.pos /= normalize_r
        #     b.pos += Vector2D(400, 400)
    
    def update(self):
        for i in range(N):
            for j in range(i+1, N):
                r1 = self.bodies[i].get_pos()
                r2 = self.bodies[j].get_pos()

                m1 = self.bodies[i].mass
                m2 = self.bodies[j].mass


                r = r2 - r1
                if r.magnitude() == 0:
                    r = Vector2D(1e-6, 1e-6)
                r_sq = r.x * r.x + r.y * r.y
                r_mag = math.sqrt(r_sq)

                # tmp = G * (m1 * m2 / max(r_sq, 0.1))
                tmp = r * G / (max(r_sq, 0.1) * r_mag)
                # force = r.normalize() * tmp

                # print(force)

                self.bodies[i].acc += tmp * m2
                self.bodies[j].acc -= tmp * m1

        for i in range(N):
            self.bodies[i].update(dt)
            
    
    def __repr__(self):
        return f"""
        Body 1 - Position: {self.bodies[0].pos}, Velocity: {self.bodies[0].vel}, Acceleration: {self.bodies[0].acc}, Mass: {self.bodies[0].mass}\n
        Body 2 - Position: {self.bodies[1].pos}, Velocity: {self.bodies[1].vel}, Acceleration: {self.bodies[1].acc}, Mass: {self.bodies[1].mass}
        """
    def get_bodies(self):
        return self.bodies
    


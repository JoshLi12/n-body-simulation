import numpy as np
from body import Body
from vector import Vector2D
import math
import random


dt = 0.05
radius = 2
N = 150
v = 1.0
m = 1.0
G = 5
sd = 100

class Simulation():
    def __init__(self):
        self.bodies = []

        def rand_pos():
            theta = random.randint(0, 1000)/1000 * 2 * math.pi
            return Vector2D(400 + math.cos(theta) * random.randint(1, sd), 400 + math.sin(theta) * random.randint(0,sd))
        
        def rand_vel():
            theta = random.randint(0, 1000)/1000 * 2 * math.pi
            return Vector2D(math.cos(theta), math.sin(theta))


        for i in range(N):
            pos = rand_pos()
            vel = rand_vel()
            self.bodies.append(Body(pos, vel, m, radius))

        # com_vel = sum((b.vel * b.mass for b in self.bodies), Vector2D(0,0))/N
        # com_pos = sum((b.pos * b.mass for b in self.bodies), Vector2D(0,0))/N

        # for b in self.bodies:
        #     b.vel -= com_vel
        #     b.pos -= com_pos
        #     b.pos += Vector2D(400, 400)

        # normalize_r = max(b.pos.magnitude() for b in self.bodies)

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
                    r = Vector2D(random.randint(-1, 1)/1000, random.randint(-1, 1)/1000)
                r_sq = r.x * r.x + r.y * r.y

                tmp = G * (m1 * m2 / max(r_sq, 0.001))
                force = r.normalize() * tmp

                # print(force/m2)

                self.bodies[i].acc -= force / m2
                self.bodies[j].acc += force / m1

        for i in range(N):
            self.bodies[i].update(dt)
            
    
    def __repr__(self):
        return f"""
        Body 1 - Position: {self.bodies[0].pos}, Velocity: {self.bodies[0].vel}, Acceleration: {self.bodies[0].acc}, Mass: {self.bodies[0].mass}\n
        Body 2 - Position: {self.bodies[1].pos}, Velocity: {self.bodies[1].vel}, Acceleration: {self.bodies[1].acc}, Mass: {self.bodies[1].mass}
        """
    def get_bodies(self):
        return self.bodies
    


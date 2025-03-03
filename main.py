from body import Body
from simulation import Simulation
from vector import Vector2D
import numpy as np

def main():
    simulation = Simulation()
    while True:
        # print(simulation.bodies[0])
        # print(simulation.bodies[1])
        simulation.update()

if __name__ == "__main__":
    main()


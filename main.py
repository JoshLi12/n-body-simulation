from body import Body
from simulation import Simulation
from vector import Vector2D
import numpy as np

def main():
    simulation = Simulation()
    i = 1
    while True:
        
        print("Iteration",i)
        print(simulation)
        simulation.update()
        i += 1
    

if __name__ == "__main__":
    main()


import sys
import math
from typing import List

# OrderedPair contains two float fields corresponding to
# the x and y coordinates of a point or vector in two-dimensional space.
class OrderedPair:
    def __init__(self, x: float = 0.0, y: float = 0.0):
        self.x = x
        self.y = y

# Boid represents our "bird" object. It contains three
# OrderedPair fields corresponding to its position, velocity, and acceleration.
class Boid:
    def __init__(self):
        self.position = OrderedPair()
        self.velocity = OrderedPair()
        self.acceleration = OrderedPair()

# Sky represents a single time point of the simulation.
# It contains a width parameter indicating the boundary of the sky, as well as a list of Boid objects.
# It also contains the system parameters.
class Sky:
    def __init__(self):
        self.width: float = 0.0
        self.boids: List[Boid] = []
        self.max_boid_speed: float = 0.0  # fastest speed that a boid can fly
        self.proximity: float = 0.0       # used to determine if boids are close enough for forces to apply
        self.separation_factor: float = 0.0
        self.alignment_factor: float = 0.0
        self.cohesion_factor: float = 0.0
            

# write your net_acceleration_due_to_cohesion() function here along with any subroutines that you need.
def net_acceleration_due_to_cohesion(current_sky: Sky, i: int) -> OrderedPair:
    """
    Compute the net acceleration due to cohesion for a boid.

    Args:
        current_sky: A Sky object containing boids, proximity, and cohesionFactor.
        i: Index of the boid of interest in current_sky.boids.
    Returns:
        An OrderedPair representing the acceleration component due to
        cohesive forces acting on the boid at index i.
    Fx = ccohesion · (x2 − x1)/d
    """
    
    x_force_sum=0
    y_force_sum=0
    cur_boid=current_sky.boids[i]
    count=0

    for boid in current_sky.boids:
        if ((distance(cur_boid.position,boid.position))<current_sky.proximity) and (distance(cur_boid.position,boid.position)!=0):
            x_force_sum+=current_sky.cohesion_factor*(cur_boid.position.x-boid.position.x)/(distance(cur_boid.position,boid.position))
            y_force_sum+=current_sky.cohesion_factor*(cur_boid.position.y-boid.position.y)/(distance(cur_boid.position,boid.position))
            count+=1

    x_force=x_force_sum/(count)
    y_force=y_force_sum/(count)
    accel=OrderedPair(-x_force,-y_force)
    return accel

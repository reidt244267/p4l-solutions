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

            
#implement update_acceleration and note use of subroutines
def update_acceleration(current_sky: Sky, i: int) -> OrderedPair:
    """
    Update the acceleration of a boid in the next generation.

    Args:
        current_sky: A Sky object containing boids and behavioral parameters.
        i: Index of the boid of interest in current_sky.boids.
    Returns:
        An OrderedPair representing the updated acceleration of the boid
        at index i for the next generation.
    """
    if count_thershold(current_sky,i)==False:
        return OrderedPair(0.0,0.0)
    sep_accel=net_acceleration_due_to_separation(current_sky,i)
    align_accel=net_acceleration_due_to_alignment(current_sky,i)
    coh_accel=net_acceleration_due_to_cohesion(current_sky,i)

    net_x_accel=sep_accel.x+align_accel.x+coh_accel.x
    net_y_accel=sep_accel.y+align_accel.y+coh_accel.y
    return OrderedPair(net_x_accel,net_y_accel)




def count_thershold(current_sky: Sky, i: int):
    count=0
    for boid in current_sky.boids:
        if distance(boid.position,current_sky.boids[i].position)<current_sky.proximity:
            count+=1
    if count>0:
        return True
    else:
        return False

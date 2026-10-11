import sys
import math
from typing import List

# OrderedPair contains two float fields corresponding to
# the x and y coordinates of a point or vector in two-dimensional space.
class OrderedPair:
    def __init__(self, x: float = 0.0, y: float = 0.0):
        self.x = x
        self.y = y

# Boid represents our "bird" object. It contains two
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

            
# write your update_velocity() function here along with any subroutines that you need.
def update_velocity(b: Boid, old_acceleration: OrderedPair, max_boid_speed: float, time_step: float) -> OrderedPair:
    """
    Update the velocity of a boid.

    Args:
        b: A Boid object.
        old_acceleration: An OrderedPair representing the previous acceleration.
        time_step: The time step over which to update the velocity.
        max_boid_speed: The maximum allowed speed of the boid.
    Returns:
        An OrderedPair representing the updated velocity of the boid after
        time_step seconds.
        vx(n+1) = (1/2) · (ax(n) + ax(n+1)) · t + vx(n)
    """

    vel_x=((0.5)*(old_acceleration.x+b.acceleration.x)*time_step)+b.velocity.x
    vel_y=((0.5)*(old_acceleration.y+b.acceleration.y)*time_step)+b.velocity.y

    


    return limit_speed(OrderedPair(vel_x,vel_y),max_boid_speed)

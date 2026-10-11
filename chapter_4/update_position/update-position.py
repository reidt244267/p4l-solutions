import sys

# OrderedPair contains two float fields corresponding to
# the x and y coordinates of a point or vector in two-dimensional space.
class OrderedPair:
    def __init__(self, x=0.0, y=0.0):
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


# write your update_position() function here along with any subroutines that you need.
def update_position(
    b : Boid,
    old_acceleration : OrderedPair,
    old_velocity : OrderedPair,
    sky_width: float,
    time_step: float
) -> OrderedPair:
    """
    Update the position of a boid.

    Args:
        b: A Boid object.
        old_acceleration: An OrderedPair representing the previous acceleration.
        old_velocity: An OrderedPair representing the previous velocity.
        sky_width: The width of the sky (used for wrap-around behavior).
        time_step: The time step over which to update the position.
    Returns:
        An OrderedPair representing the updated position of the boid after
        time_step seconds, with wrap-around at the sky boundaries.
        px(n+1) = (1/2) · ax(n) · t2 + vx(n) · t + px(n)
    """
    pos_x=((0.5)*old_acceleration.x*(time_step**2))+(old_velocity.x*time_step)+b.position.x
    pos_y=((0.5)*old_acceleration.y*(time_step**2))+(old_velocity.y*time_step)+b.position.y

    while(pos_x<0):
        pos_x=sky_width+pos_x
    while(pos_x>sky_width):
        pos_x=pos_x-sky_width

    while(pos_y<0):
        pos_y=sky_width+pos_y
    while(pos_y>sky_width):
        pos_y=pos_y-sky_width
        



    return OrderedPair(pos_x,pos_y)

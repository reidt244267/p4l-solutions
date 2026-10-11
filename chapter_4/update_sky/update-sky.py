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

            
# implement update_sky
def update_sky(current_sky: Sky, time_step: float) -> Sky:
    """
    Update a sky of boids by one time step.

    Args:
        current_sky: A Sky object containing boids and simulation parameters.
        time_step: The time step for the update.
    Returns:
        The updated Sky after one time step.
        simulate_boids
└── update_sky
    ├── update_acceleration
    │   ├── net_acceleration_due_to_separation
    │   ├── net_acceleration_due_to_alignment
    │   └── net_acceleration_due_to_cohesion
    ├── update_velocity (b: Boid, old_acceleration: OrderedPair, max_boid_speed: float, time_step: float)
    │   └── limit_speed
    └── update_position update_position(
    b : Boid,
    old_acceleration : OrderedPair,
    old_velocity : OrderedPair,
    sky_width: float,
    time_step: float
)
        └── (torus wrapping)
└── (utility used throughout) sum_vectors, distance
    """
    new_sky=copy_sky(current_sky)
    for i in range(len(current_sky.boids)):
        old_accel=current_sky.boids[i].acceleration
        old_vel=current_sky.boids[i].velocity
        new_accel=update_acceleration(current_sky,i)
        new_sky.boids[i].acceleration.x = new_accel.x
        new_sky.boids[i].acceleration.y = new_accel.y
        new_vel=update_velocity(new_sky.boids[i],old_accel,current_sky.max_boid_speed,time_step)
        new_sky.boids[i].velocity.x = new_vel.x
        new_sky.boids[i].velocity.y = new_vel.y
        new_pos=update_position(new_sky.boids[i],old_accel,old_vel,current_sky.width,time_step)
        new_sky.boids[i].position.x = new_pos.x
        new_sky.boids[i].position.y = new_pos.y
        
        

    return new_sky

def copy_sky(current_sky: Sky) -> Sky:
    """
    Create a copy of a sky.

    Args:
        current_sky: A Sky object to copy.
    Returns:
        A new Sky object with all boids and parameters copied from current_sky.
    """
    new_sky = Sky()
    new_sky.width = current_sky.width
    new_sky.max_boid_speed = current_sky.max_boid_speed
    new_sky.proximity = current_sky.proximity
    new_sky.separation_factor = current_sky.separation_factor
    new_sky.alignment_factor = current_sky.alignment_factor
    new_sky.cohesion_factor = current_sky.cohesion_factor
    new_sky.boids = [Boid() for _ in range(len(current_sky.boids))]

    for i in range(len(current_sky.boids)):
        new_sky.boids[i].position.x = current_sky.boids[i].position.x
        new_sky.boids[i].position.y = current_sky.boids[i].position.y
        new_sky.boids[i].velocity.x = current_sky.boids[i].velocity.x
        new_sky.boids[i].velocity.y = current_sky.boids[i].velocity.y
        new_sky.boids[i].acceleration.x = current_sky.boids[i].acceleration.x
        new_sky.boids[i].acceleration.y = current_sky.boids[i].acceleration.y

    return new_sky

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

def net_acceleration_due_to_separation(current_sky: Sky, i: int) -> OrderedPair:
    """
    Compute the net acceleration due to separation for a boid.

    Args:
        current_sky: A Sky object containing boids, proximity, and separationFactor.
        i: Index of the boid of interest in current_sky.boids.
    Returns:
        An OrderedPair representing the acceleration component due to
        separation forces acting on the boid at index i.
        Fx = cseparation · (x1 − x2)/d2
    """
    x_force_sum=0
    y_force_sum=0
    cur_boid=current_sky.boids[i]
    count=0
    for boid in current_sky.boids:
        if ((distance(cur_boid.position,boid.position))<current_sky.proximity) and (distance(cur_boid.position,boid.position)!=0):
            x_force_sum+=current_sky.separation_factor*(cur_boid.position.x-boid.position.x)/(distance(boid.position,cur_boid.position)**2)
            y_force_sum+=current_sky.separation_factor*(cur_boid.position.y-boid.position.y)/(distance(boid.position,cur_boid.position)**2)
            count+=1


    x_force=x_force_sum/(count)
    y_force=y_force_sum/(count)
    accel=OrderedPair(x_force,y_force)
    return accel

def net_acceleration_due_to_alignment(current_sky: Sky, i: int) -> OrderedPair:
    """
    Compute the net acceleration due to alignment for a boid.

    Args:
        current_sky: A Sky object containing boids, proximity, and alignmentFactor.
        i: Index of the boid of interest in current_sky.boids.
    Returns:
        An OrderedPair representing the acceleration component due to
        alignment forces acting on the boid at index i.
        Fx = calignment · vx/d
    """
    x_force_sum=0
    y_force_sum=0
    cur_boid=current_sky.boids[i]
    count=0
    for boid in current_sky.boids:
        if ((distance(cur_boid.position,boid.position))<current_sky.proximity) and (distance(cur_boid.position,boid.position)!=0):
            x_force_sum+=current_sky.alignment_factor*(boid.velocity.x)/distance(cur_boid.position,boid.position)
            y_force_sum+=current_sky.alignment_factor*(boid.velocity.y)/distance(cur_boid.position,boid.position)
            count+=1


    x_force=x_force_sum/(count)
    y_force=y_force_sum/(count)
    accel=OrderedPair(x_force,y_force)
    return accel

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

def limit_speed(vel : OrderedPair, max_speed: float) -> OrderedPair:
    """
    Limit the speed of a boid.

    Args:
        max_speed: The maximum allowed speed.
        vel: An OrderedPair representing the velocity vector.
    Returns:
        An OrderedPair representing the velocity after limiting its
        magnitude to max_speed, if necessary.
    """
    speed=math.sqrt((vel.x**2)+(vel.y**2))
    if speed>max_speed:
        return OrderedPair((vel.x*(max_speed/speed)),(vel.y*(max_speed/speed)))
    else:
        return vel

def distance(p1: OrderedPair, p2: OrderedPair) -> float:
    """
    Compute the distance between two points.

    Args:
        p1: An ordered pair (x, y).
        p2: An ordered pair (x, y).
    Returns:
        The distance between p1 and p2.
    """
    return math.sqrt((p1.x-p2.x)**2+(p1.y-p2.y)**2)

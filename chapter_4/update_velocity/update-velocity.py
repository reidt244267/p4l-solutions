from dataclasses import dataclass, field
        
@dataclass
class OrderedPair:
    x: float = 0.0
    y: float = 0.0

@dataclass
class Body:
    name: str = ""
    position: OrderedPair = field(default_factory=OrderedPair)
    velocity: OrderedPair = field(default_factory=OrderedPair)
    acceleration: OrderedPair = field(default_factory=OrderedPair)
    mass: float = 0.0
    radius: float = 0.0
    red: int = 0
    green: int = 0
    blue: int = 0


# Write your update_velocity() function here along with any subroutines you need.
def update_velocity(b: Body, old_acceleration: OrderedPair, time: float) -> OrderedPair:
    """
    Update the velocity of a body using Newtonian kinematics.

    Args:
        b: A Body object.
        time: The amount of time elapsed.
    Returns:
        An OrderedPair representing the updated velocity of the body.
    """
    vx=b.velocity.x+0.5*(b.acceleration.x+old_acceleration.x)*time
    vy=b.velocity.y+0.5*(b.acceleration.y+old_acceleration.y)*time

    return OrderedPair(vx,vy)

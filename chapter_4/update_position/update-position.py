from dataclasses import dataclass, field
# Define your classes and UpdatePosition function here

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

        
# Write your update_position() function here
def update_position(b: Body, old_acc: OrderedPair, old_vel: OrderedPair, time: float) -> OrderedPair:
    """
    Update the position of a body using Newtonian kinematics.

    Args:
        b: A Body object.
        old_acceleration: An OrderedPair representing the previous acceleration.
        old_velocity: An OrderedPair representing the previous velocity.
        time: The amount of time elapsed.
    Returns:
        An OrderedPair representing the updated position of the body.
    """

    px=b.position.x+old_vel.x*time+0.5*old_acc.x*(time**2)
    py=b.position.y+old_vel.y*time+0.5*old_acc.y*(time**2)

    return OrderedPair(px,py)

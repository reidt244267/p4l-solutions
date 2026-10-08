import math
import sys
from dataclasses import dataclass, field

G = 2 * 6.67408e-11

@dataclass
class OrderedPair:
    x: float = 0.0
    y: float = 0.0

@dataclass
class Body:
    name: str = ""
    mass: float = 0.0
    radius: float = 0.0
    position: OrderedPair = field(default_factory=OrderedPair)
    velocity: OrderedPair = field(default_factory=OrderedPair)
    acceleration: OrderedPair = field(default_factory=OrderedPair)
    red: int = 0
    green: int = 0
    blue: int = 0

@dataclass
class Universe:
    bodies: list[Body] = field(default_factory=list)
    width: float = 0.0

# Insert your update_acceleration() function here, along with any subroutines that you need.
def update_acceleration(current_universe: Universe, b: Body) -> OrderedPair:
    """
    Compute the updated acceleration of a body due to the gravity of every
    other body in the universe.

    Newton's second law: F = ma, so a = F_net / m.

    Args:
        current_universe: A Universe object (a collection of Body objects).
        b: The Body whose acceleration is being updated.
    Returns:
        An OrderedPair representing the body's new acceleration.
    """
    net_force=compute_net_force(current_universe,b)

    ax=net_force.x/b.mass
    ay=net_force.y/b.mass

    return OrderedPair(ax,ay)

def copy_universe(current_universe: Universe) -> Universe:
    """
    Create a copy of a universe.

    Args:
        current_universe: A Universe object to copy.
    Returns:
        A new Universe object with copied width and bodies.
    """
    new_universe = Universe()
    new_universe.width = current_universe.width
    new_universe.bodies = [copy_body(body) for body in current_universe.bodies]
    return new_universe


def copy_body(old_body: Body) -> Body:
    """
    Create a copy of a body.

    Args:
        old_body: A Body object to copy.
    Returns:
        A new Body object with all fields copied from old_body.
    """
    new_body = Body()
    new_body.mass = old_body.mass
    new_body.name = old_body.name
    new_body.position.x = old_body.position.x
    new_body.position.y = old_body.position.y
    new_body.velocity.x = old_body.velocity.x
    new_body.velocity.y = old_body.velocity.y
    new_body.acceleration.x = old_body.acceleration.x
    new_body.acceleration.y = old_body.acceleration.y
    return new_body

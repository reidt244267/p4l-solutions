import sys
import math
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
    gravitational_constant: float = G
        
# write your compute_net_force() function here along with any subroutines that you need.
def compute_net_force(current_universe : Universe, b : Body) -> OrderedPair:
    """
    Compute the net force acting on a body from all bodies in a universe.

    Args:
        current_universe: A Universe object (a collection of Body objects).
        b: A Body object.
    Returns:
        An OrderedPair representing the net force acting on b due to all
        bodies in current_universe.
    """
    net_force=OrderedPair(0.0,0.0)

    G=current_universe.gravitational_constant

    for cur_body in current_universe.bodies:
        if cur_body is not b:
            current_force=compute_force(b, cur_body,G)
            net_force.x+=current_force.x
            net_force.y+=current_force.y

    return net_force


def compute_force(b1,b2,G):
    d=distance(b1.position,b2.position)

    if d==0.0:
        return OrderedPair(0.0,0.0)

    F_magnitude=G*b1.mass*b2.mass/(d*d)

    dx=b2.position.x-b1.position.x
    dy=b2.position.y-b1.position.y

    Fx=F_magnitude*(dx/d)
    Fy=F_magnitude*(dy/d)
    return OrderedPair(Fx,Fy)

def distance(p1,p2):
    return math.sqrt((p1.x-p2.x)**2+(p1.y-p2.y)**2)

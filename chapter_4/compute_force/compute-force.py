import math

# Constants
G = 2 * 6.67408  # Gravitational constant

class OrderedPair:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y


class Body:
    def __init__(self, name, mass, position):
        self.name = name
        self.mass = mass
        self.position = position
        self.radius = 0.0
        self.velocity = OrderedPair(0.0, 0.0)
        self.acceleration = OrderedPair(0.0, 0.0)
        self.red = 0
        self.green = 0
        self.blue = 0


# Write your compute_force() function here along with any subroutines that you need.
def compute_force(b1: Body, b2: Body, G: float) -> OrderedPair:
    """
    Compute the gravitational force exerted on one body by another.

    Args:
        b1: The first Body.
        b2: The second Body.
        G: The gravitational constant.
    Returns:
        An OrderedPair representing the gravitational force on b1
        exerted by b2.
    """
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

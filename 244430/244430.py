import math

class OrderedPair:
    """
    Represents a 2D point or vector with x and y coordinates.

    Attributes:
        x (float): The x-coordinate.
        y (float): The y-coordinate.
    """
    def __init__(self, x: float = 0.0, y: float = 0.0):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"OrderedPair({self.x}, {self.y})"


class Body:
    """
    Represents a circular body in 2D space with a position and radius.

    Attributes:
        p (OrderedPair): The position of the body's center.
        radius (float): The radius of the body.
    """
    def __init__(self, p: OrderedPair, radius: float):
        self.p = p
        self.radius = radius

    def __repr__(self) -> str:
        return f"Body(p={self.p}, radius={self.radius})"


def distance(p0: OrderedPair, p1: OrderedPair) -> float:
    """Compute the Euclidean distance between two OrderedPair points."""
    dx = p0.x - p1.x
    dy = p0.y - p1.y
    return math.sqrt(dx * dx + dy * dy)


def are_overlapping(b1: Body, b2: Body) -> bool:
    """
    Determine whether two circular Body objects overlap.

    Input:
        b1 (Body): The first circular body with attributes p (OrderedPair) and radius (float).
        b2 (Body): The second circular body with attributes p (OrderedPair) and radius (float).

    Output:
        bool: True if the circles overlap (d < b1.radius + b2.radius), False otherwise.
    """
    if distance(b1.p,b2.p)<(b1.radius+b2.radius):
        return True
    else:
        return False

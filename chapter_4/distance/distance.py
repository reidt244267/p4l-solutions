import math # can use the math package to help

# Define OrderedPair class
class OrderedPair:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

# Write your distance() function here
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

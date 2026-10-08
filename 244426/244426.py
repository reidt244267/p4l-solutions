import math

class Circle:
    """
    Represents a 2D circle via its center and radius.

    Attributes:
        x1: the x-coordinate of the center (float)
        y1: the y-coordinate of the center (float)
        radius: the circle's radius (float)

    Class Attributes:
        description: describes some characteristic of the object (string) 
    """

    description: str = "round"

    def __init__(self, x1: float=0, y1: float=0, radius: float=0):
        if radius < 0.0:
            raise ValueError("radius must be nonnegative.")
        self.x1 = x1
        self.y1 = y1
        self.radius = radius

    def __repr__(self) -> str:
        return f"Circle(x1={self.x1}, y1={self.y1}, radius={self.radius})"

def distance(x1 : float, y1 : float, x2 : float, y2 : float) -> float:
    """
    Compute the Euclidean distance between two points in 2D space.
    Input:
        (x1 : float, y1 : float): The first point, with x and y coordinates.
        (x2 : float, y2 : float): The second point, with x and y coordinates.
    Output:
        float: The Euclidean distance between p0 and p1.
    """
    dx = x1 - x2
    dy = y1 - y2
    return math.sqrt(dx * dx + dy * dy)

def contains_point_circle(c: Circle, x: float, y: float) -> bool:
    """
    Determine whether a point (x, y) lies inside or on the boundary of a Circle object.

    Input:
        c (Circle): The circle, defined by center coordinates (c.x1, c.y1) and radius c.radius.
        x (float): The x-coordinate of the point to test.
        y (float): The y-coordinate of the point to test.

    Output:
        bool: True if the point is inside or on the circle's boundary, False otherwise.
    """
    if distance(x,y,c.x1,c.y1)>c.radius:
        return False
    else:
        return True

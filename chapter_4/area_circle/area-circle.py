import math
# Chapter 4 Check Your Work: Introduction to Classes.
#
# The Circle class from the code along is provided below. As in the code
# along, use 3.0 for pi (we will fix that in a later chapter).

class Circle:
    """
    Represents a 2D circle defined by its center and radius.

    Attributes:
        x1 (float): The x-coordinate of the circle's center.
        y1 (float): The y-coordinate of the circle's center.
        radius (float): The radius of the circle. Must be non-negative.
    """

    def __init__(self, x1: float = 0.0, y1: float = 0.0, radius: float = 0.0) -> None:
        if radius < 0.0:
            raise ValueError("radius must be non-negative")

        self.x1 = x1
        self.y1 = y1
        self.radius = radius

    def __repr__(self) -> str:
        return f"Circle(x1={self.x1}, y1={self.y1}, radius={self.radius})"


def area_circle(c: Circle) -> float:
    """
    Compute the area of a circle.

    Args:
        c (Circle): The circle whose area to compute.
            Must have a `radius` attribute.

    Returns:
        float: The area of the circle, calculated as 3.0 × radius².
    """
    return 3*(c.radius**2)

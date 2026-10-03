# Chapter 4 Check Your Work: Introduction to Classes.
#
# This is the exercise posed in the code along. The Circle class is
# provided below. As in area_circle(), use 3.0 for pi.

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


def perimeter_circle(c: Circle) -> float:
    """
    Compute the perimeter (circumference) of a circle.

    Args:
        c (Circle): The circle whose perimeter to compute.
            Must have a `radius` attribute.

    Returns:
        float: The perimeter of the circle, calculated as 2 × 3.0 × radius.
    """
    return 2*3*c.radius

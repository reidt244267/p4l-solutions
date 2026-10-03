# Chapter 4 Check Your Work: Introduction to Classes.
#
# Objects are pass by reference: change c's attributes inside the function
# and the caller sees the change. The function returns nothing; we check
# the circle you were given after your function runs.

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


def translate_circle(c: Circle, a: float, b: float) -> None:
    """
    Translate a circle by shifting its center coordinates in place.

    This function mutates the given circle by adjusting its
    `x1` and `y1` attributes directly.

    Args:
        c (Circle): The circle to translate.
            Must have `x1` and `y1` attributes representing its center.
        a (float): The amount to shift along the x-axis.
        b (float): The amount to shift along the y-axis.

    Returns:
        None
    """
    c.x1=c.x1+a
    c.y1=c.y1+b
    pass

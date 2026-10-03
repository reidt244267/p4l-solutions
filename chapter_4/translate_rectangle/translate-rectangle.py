# Chapter 4 Check Your Work: Introduction to Classes.
#
# Objects are pass by reference: change r's attributes inside the function
# and the caller sees the change. The function returns nothing; we check
# the rectangle you were given after your function runs.

class Rectangle:
    """
    Represents a 2D rectangle with width, height, position, and rotation.

    Attributes:
        width (float): The rectangle's width. Must be non-negative.
        height (float): The rectangle's height. Must be non-negative.
        x1 (float): The x-coordinate of the rectangle's origin or corner.
        y1 (float): The y-coordinate of the rectangle's origin or corner.
        rotation (float): The rectangle's rotation angle in degrees.
    """

    def __init__(self, width: float = 0.0, height: float = 0.0,
                 x1: float = 0.0, y1: float = 0.0, rotation: float = 0.0) -> None:
        if width < 0.0:
            raise ValueError("width must be non-negative")
        if height < 0.0:
            raise ValueError("height must be non-negative")

        self.width = width
        self.height = height
        self.x1 = x1
        self.y1 = y1
        self.rotation = rotation

    def __repr__(self) -> str:
        return (f"Rectangle(width={self.width}, height={self.height}, "
                f"x1={self.x1}, y1={self.y1}, rotation={self.rotation})")


def translate_rectangle(r: Rectangle, a: float, b: float) -> None:
    """
    Translate a rectangle by shifting its coordinates in place.

    This function mutates the given rectangle by adjusting its
    `x1` and `y1` attributes directly.

    Args:
        r (Rectangle): The rectangle to translate.
            Must have `x1` and `y1` attributes representing its position.
        a (float): The amount to shift along the x-axis.
        b (float): The amount to shift along the y-axis.

    Returns:
        None
    """
    r.x1=r.x1+a
    r.y1=r.y1+b

    pass

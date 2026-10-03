# Chapter 4 Check Your Work: Introduction to Classes.
#
# The Rectangle class from the code along is provided below. Read a
# rectangle's attributes with dot notation, as in r.width.

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


def area_rectangle(r: Rectangle) -> float:
    """
    Compute the area of a rectangle.

    Args:
        r (Rectangle): The rectangle whose area to compute.
            Must have `width` and `height` attributes.

    Returns:
        float: The area of the rectangle, calculated as width × height.
    """
    return r.width*r.height

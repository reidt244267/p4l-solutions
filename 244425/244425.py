#don't edit the class (could result in the autograder failing)
class Rectangle:
    """
    Represents a 2D rectangle with width, height, position, and rotation

    Attributes:
        width: (float)
        height: (float)
        x1: the x-coordinate of the rectangle's origin (float)
        y1: the y-coordinate of the rectangle's origin (float)
        rotation: rotation of shape in degrees (float)

    Class Attributes:
        description: describes some characteristic of the object (string) 
    """

    description: str = "boxy"

    def __init__(self, width: float=0.0, height: float=0.0, x1: float=0, y1: float=0, rotation: float=0):
        if width < 0.0 or height < 0.0:
            raise ValueError("width and height must be nonnegative.")
        self.width = width
        self.height = height
        self.x1 = x1
        self.y1 = y1
        self.rotation = rotation

    def __repr__(self) -> str:
        return f"Rectangle(width={self.width},height={self.height},x1={self.x1},y1={self.y1},rotation={self.rotation})"

def scale_rectangle(r: Rectangle, factor: float) -> None:
    """
    Scale a Rectangle object’s size in place while keeping its position and rotation unchanged.

    Input:
        r (Rectangle): The rectangle to scale, with attributes width and height.
        factor (float): The scale factor to apply to the rectangle’s width and height.

    Output:
        None: The rectangle is modified directly (not returned).

    Rules:
        - Multiply both width and height by factor.
        - Do not change x1, y1, or rotation.
        - Raise ValueError: Scale factor must be nonnegative. if factor is negative.
    """
    if factor<0:
        raise ValueError("Scale factor must be nonnegative.")

    r.width=r.width*factor
    r.height=r.height*factor
    return 

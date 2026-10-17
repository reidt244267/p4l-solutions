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

    def __init__(self, width: float=0.0, height: float=0.0, x1: float=0.0, y1: float=0.0, rotation: float=0.0):
        if width < 0.0 or height < 0.0:
            raise ValueError("width and height must be nonnegative.")
        self.width = width
        self.height = height
        self.x1 = x1
        self.y1 = y1
        self.rotation = rotation

    def __repr__(self) -> str:
        return f"Rectangle(width={self.width},height={self.height},x1={self.x1},y1={self.y1},rotation={self.rotation})"


class Circle:
    """
    Represents a 2D circle via its center and radius.

    Attributes:
        x1: the x-coordinate of the center (float)
        y1: the y-coordinate of the center (float)
        radius: the center's radius (float)

    Class Attributes:
        description: describes some characteristic of the object (string) 
    """

    description: str = "round"

    def __init__(self, x1: float=0, y1: float = 0, radius: float = 0):
        if radius < 0.0:
            raise ValueError("width and height must be nonnegative.")
        self.x1 = x1
        self.y1 = y1
        self.radius = radius

    def __repr__(self) -> str:
        return f"Circle(x1={self.x1}, y1={self.y1}, radius={self.radius})"

    # IMPLEMENT THIS METHODD!!!!!
    def bbox(self) -> Rectangle:
        """
        Return the axis-aligned bounding box of the circle as a Rectangle with rotation = 0.0.

        Input:
            None (uses the circle’s own attributes).

        Output:
            Rectangle: A rectangle whose width and height equal the circle’s diameter (2 * radius), fully                   encloses the circle and with rotation = 0.0.
            self, width: float=0.0, height: float=0.0, x1: float=0.0, y1: float=0.0, rotation: float=0.0):
        """

        return Rectangle(self.radius*2, self.radius*2, self.x1-self.radius, self.y1-self.radius, 0.0)

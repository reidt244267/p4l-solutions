import math   # likely useful

def rotate_point_ccw(p: tuple[float, float],
                     pivot: tuple[float, float],
                     rotation_angle: float) -> tuple[float, float]:
    """
    Rotate point p about pivot by 'rotation_angle' degrees counter-clockwise.

    Parameters:
        p (tuple[float, float]): The point (x, y).
        pivot (tuple[float, float]): The pivot (cx, cy).
        rotation_angle (float): Rotation angle in degrees (CCW positive).

    Returns:
        tuple[float, float]: Rotated point (x', y').
        x′ = (x − cx)·cos(θ) − (y − cy)·sin(θ) + cx
y′ = (x − cx)·sin(θ) + (y − cy)·cos(θ) + cy

2. Python’s math.sin() and math.cos() functions expect radians, not degrees. You can use

theta = math.radians(angle)
    """
    theta=math.radians(rotation_angle)
    new_x=(p[0]-pivot[0])*math.cos(theta)-(p[1]-pivot[1])*math.sin(theta)+pivot[0]
    new_y=(p[0]-pivot[0])*math.sin(theta)+(p[1]-pivot[1])*math.cos(theta)+pivot[1]

    return (new_x, new_y)

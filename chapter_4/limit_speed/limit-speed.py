        
import sys
import math

# Please do not remove these definitions. You may add to them if needed.

class OrderedPair:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

# write your limit_speed() function here along with any subroutines that you need.
def limit_speed(vel : OrderedPair, max_speed: float) -> OrderedPair:
    """
    Limit the speed of a boid.

    Args:
        max_speed: The maximum allowed speed.
        vel: An OrderedPair representing the velocity vector.
    Returns:
        An OrderedPair representing the velocity after limiting its
        magnitude to max_speed, if necessary.
    """
    speed=math.sqrt((vel.x**2)+(vel.y**2))
    if speed>max_speed:
        return OrderedPair((vel.x*(max_speed/speed)),(vel.y*(max_speed/speed)))
    else:
        return vel

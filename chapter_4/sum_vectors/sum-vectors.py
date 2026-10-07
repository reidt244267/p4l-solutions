import sys
from typing import List

# OrderedPair contains two float fields corresponding to
# the x and y coordinates of a point or vector in 2D space.
class OrderedPair:
    def __init__(self, x: float = 0.0, y: float = 0.0) -> None:
        self.x = x
        self.y = y

def sum_vectors(vectors: List[OrderedPair]) -> OrderedPair:
    """
    Sum multiple vectors.

    Args:
        vectors: A list of OrderedPair vectors.
    Returns:
        An OrderedPair representing the sum of all vectors in the list.
    """
    xs=0
    ys=0
    for orderedpair in vectors:
        xs+=orderedpair.x
        ys+=orderedpair.y

    return OrderedPair(xs,ys)

from dataclasses import dataclass
from typing import Self

@dataclass
class Node:
    """
    A node in a binary phylogenetic tree (used as a cluster in UPGMA).

    Attributes:
        num: Numeric identifier for the node.
        age: Age (height) of the node.
        label: Optional label (e.g., species name for leaves).
        child1: Left child node, or None if this node is a leaf.
        child2: Right child node, or None if this node is a leaf.
    """
    num: int = 0
    age: float = 0.0
    label: str = ""
    child1: Self | None = None
    child2: Self | None = None

    def is_leaf(self) -> bool:
        """Return whether this node is a leaf (i.e., has no children)."""
        return self.child1 is None and self.child2 is None

    def count_leaves(self) -> int:
        """
        Students: implement this method.

        Recursively count the number of leaves in the subtree rooted at this node.
        A leaf is a node with no children (both child1 and child2 are None).

        Returns:
            int: Number of leaf nodes under (and including) this node.
        """
        count=0


        if self.is_leaf():
            return 1
        elif self.child1==None:
            count=count+self.child2.count_leaves()
        elif self.child2==None:
            count=count+self.child1.count_leaves()
        else:
            count=count+self.child1.count_leaves()+self.child2.count_leaves()


    

        return count
    

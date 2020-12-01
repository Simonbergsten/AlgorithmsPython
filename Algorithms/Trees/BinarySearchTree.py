"""
[X] A node can can have at most 2 leaves
[X] If node Y is larger than node X, then it has to be on the right of node X.
[X] If node Y is smaller than node X, then it has to be on the left of node X.

Three cases of deletion:
1. Deletion of a lead node - Just remove the leaf
2. Deletion of a node with one child - Delete the node and connect it's parent to it's child
3. Deletion of a node with two childs - Set the new node to the minimum of right side
"""
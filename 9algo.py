# Depth-first Search

#   You're given a NOde  class that has a  name   and an
#   array of optional  children  nodes. When put together, nodes form
#   an acyclic tree-like structure.

#     Implement the    depthFirstSearch  method on the NOde  class, which takes in an empty array, traverses the tree
#   using the Depth-first Search approach (specifically navigating the tree from
#   left to right), stores all of the nodes' names in the input array, and returns
#   it.

#   If you're unfamiliar with Depth-first Search, we recommend watching the
#   Conceptual Overview section of this question's video explanation before
#   starting to code.

# Sample Input
# graph = A
#      /  |  \
#     B   C   D
#    / \     / \
#   E   F   G   H
#      / \   \
#     I   J   K

# Sample Output
# ["A", "B", "E", "F", "I", "J", "C", "D", "G", "K", "H"]

# Do not edit the class below except
# for the depthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        # Write your code here.
        pass

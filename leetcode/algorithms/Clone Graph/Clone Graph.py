"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution(object):
    visited_m = dict()

    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None

        if self.visited_m.get(node):
            return self.visited_m[node]

        clone_node = Node(val=node.val, neighbors=[])
        self.visited_m[node] = clone_node

        for nb in node.neighbors:
            clone_node.neighbors.append(self.cloneGraph(nb))

        return clone_node

import queue


class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n


def tree_by_levels(node):
    res = []
    if not node:
        return res
    q = queue.Queue()
    q.put(node)
    while q.qsize() > 0:
        n = q.qsize()
        while n > 0:
            curr = q.get()
            res.append(curr.value)
            print(curr.value)
            if curr.left:
                q.put(curr.left)
            if curr.right:
                q.put(curr.right)
            n -= 1
    return res


tree_by_levels(
    Node(
        Node(None, Node(None, None, 4), 2),
        Node(Node(None, None, 5), Node(None, None, 6), 3),
        1,
    )
)

class DoubleListNode:

    def __init__(self, data=0, next_node=None, prev_node=None):
        self.data = data
        self.next = next_node
        self.prev = prev_node
# @exclude

    def __repr__(self):
        return '%s -> %s' % (self.data, self.next)

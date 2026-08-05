class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        values = []
        seen = {}
        current = self
        index = 0

        while current is not None:
            if id(current) in seen:
                start = seen[id(current)]
                return (
                    " -> ".join(values)
                    + f" -> (cycle back to index {start}, val {current.val})"
                )
            seen[id(current)] = index
            values.append(str(current.val))
            current = current.next
            index += 1

        return " -> ".join(values) + " -> None"

    __repr__ = __str__


class DoublyListNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

    def __str__(self):
        values = []
        seen = {}
        current = self
        index = 0

        while current is not None:
            if id(current) in seen:
                start = seen[id(current)]
                return (
                    " <-> ".join(values)
                    + f" <-> (cycle back to index {start}, val {current.val})"
                )
            seen[id(current)] = index
            values.append(str(current.val))
            current = current.next
            index += 1

        return " <-> ".join(values) + " <-> None"

    __repr__ = __str__

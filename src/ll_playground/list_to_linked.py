
from .list_node import ListNode, DoublyListNode


def list_to_linked(lst, cycle_pos=-1):
    if not lst:
        return None

    nodes = [ListNode(v) for v in lst]

    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    if cycle_pos != -1:
        nodes[-1].next = nodes[cycle_pos]

    return nodes[0]


def list_to_dll(lst, cycle_pos=-1):
    if not lst:
        return None

    nodes = [DoublyListNode(v) for v in lst]

    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
        nodes[i + 1].prev = nodes[i]

    if cycle_pos != -1:
        nodes[-1].next = nodes[cycle_pos]

        if cycle_pos == 0:
            nodes[0].prev = nodes[-1]

    return nodes[0]
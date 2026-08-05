from .list_node import ListNode

def linked_to_list(head, limit=1000):
    values = []
    current = head
    while current and len(values) < limit:
        values.append(current.val)
        current = current.next
    return values

def has_cycle(head) -> bool:
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True

    return False


def print_ll(head) -> None:
    is_doubly = hasattr(head, "prev")
    sep = " <-> " if is_doubly else " -> "

    if is_doubly and not validate_dll_links(head):
        print("WARNING: invalid dll links (prev/next mismatch detected)")

    values = []
    seen = {}
    current = head
    index = 0

    while current:
        if id(current) in seen:
            start = seen[id(current)]
            print(
                sep.join(values)
                + f"{sep}(cycle back to index {start}, val {current.val})"
            )
            return
        seen[id(current)] = index
        values.append(str(current.val))
        current = current.next
        index += 1

    print(sep.join(values) + f"{sep}None" if values else "None")


def print_dll_reverse(tail) -> None:
    values = []
    seen = {}
    current = tail
    index = 0

    while current:
        if id(current) in seen:
            start = seen[id(current)]
            print(
                " <-> ".join(values)
                + f" <-> (cycle back to index {start}, val {current.val})"
            )
            return
        seen[id(current)] = index
        values.append(str(current.val))
        current = current.prev
        index += 1

    print(" <-> ".join(values) + " <-> None" if values else "None")


def validate_dll_links(head, limit=100000) -> bool:
    seen = set()
    current = head
    count = 0

    while current and id(current) not in seen and count < limit:
        seen.add(id(current))
        if current.next is not None and current.next.prev is not current:
            return False
        current = current.next
        count += 1

    return True

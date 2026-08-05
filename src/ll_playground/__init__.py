from .list_node import ListNode, DoublyListNode
from .list_to_linked import list_to_linked, list_to_dll
from .printer import (
    linked_to_list,
    has_cycle,
    print_ll,
    print_dll_reverse,
    validate_dll_links,
)
from .list_equal import lists_equal, dlists_equal

__all__ = [
    "ListNode",
    "DoublyListNode",
    "list_to_linked",
    "list_to_dll",
    "linked_to_list",
    "has_cycle",
    "print_ll",
    "print_dll_reverse",
    "validate_dll_links",
    "lists_equal",
    "dlists_equal",
]

__version__ = "0.1.3"
__AUTHOR__ = "REHAN GUPTA (BL4Z23)"
__EMAIL__ = "BL4Z23.DEV@GMAIL.COM"
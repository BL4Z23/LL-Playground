LL Playground
A lightweight Python toolkit for building, printing, comparing, and validating linked lists.
LL Playground provides simple utilities for working with singly linked lists and doubly linked lists, making it easier to experiment with linked-list algorithms without repeatedly writing setup code and has quality-of-life as well as debugging utilities
Installation
Install LL Playground using pip:
pip install LL-Playground
Features
Build linked lists from Python iterables
Work with singly and doubly linked lists
Print linked lists in a readable format
Compare linked lists
Validate linked-list structures
Useful for experimenting with linked-list algorithms and data structures
Lightweight with a simple API

## API REFERENCE

## Quick Start

The examples below assume the LL Playground utilities have already been imported.

### Creating a Linked List

Convert a Python list into a singly or doubly linked list:

```python
linked = list_to_linked([1, 2, 3, 4, 5])

doubly_linked = list_to_dll([1, 2, 3, 4, 5])
```

Both functions can optionally create a cycle by specifying a cycle position:

```python
linked = list_to_linked([1, 2, 3, 4, 5], cycle_pos=2)

doubly_linked = list_to_dll([1, 2, 3, 4, 5], cycle_pos=2)
```

The final node will link back to the node at the specified position. If no cycle position is provided, a standard non-cyclic linked list is created.

---

### Converting to a Python List

Use `linked_to_list()` to convert a linked list back into a regular Python list:

```python
linked_to_list(list_to_linked([1, 2, 3, 4, 5]))
```

```text
[1, 2, 3, 4, 5]
```

---

### Printing Linked Lists

Use `print_ll()` to display either a singly or doubly linked list in a readable form:

```python
print_ll(list_to_linked([1, 2, 3, 4, 5]))

print_ll(list_to_dll([1, 2, 3, 4, 5]))
```

For doubly linked lists, use `print_dll_reverse()` to traverse and print the list in reverse:

```python
print_dll_reverse(list_to_dll([1, 2, 3, 4, 5]))
```

---

### Detecting Cycles

Use `has_cycle()` to check whether a linked list contains a cycle:

```python
has_cycle(list_to_linked([1, 2, 3, 4, 5]))
```

```text
False
```

With a cycle:

```python
has_cycle(list_to_linked([1, 2, 3, 4, 5], cycle_pos=2))
```

```text
True
```

---

### Comparing Linked Lists

Use `lists_equal()` to compare two singly linked lists:

```python
lists_equal(
    list_to_linked([1, 2, 3]),
    list_to_linked([1, 2, 3])
)
```

```text
True
```

For doubly linked lists, use `dlists_equal()`:

```python
dlists_equal(
    list_to_dll([1, 2, 3]),
    list_to_dll([1, 2, 3])
)
```

```text
True
```

---

### Validating Doubly Linked Lists

Use `validate_dll_links()` to verify that the `next` and `prev` links of a doubly linked list are correctly connected:

```python
validate_dll_links(list_to_dll([1, 2, 3, 4, 5]))
```

```text
True
```

---

### Creating Nodes Manually

`ListNode` and `DoublyListNode` can also be used to construct linked lists manually.

#### Singly Linked List

```python
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
```

#### Doubly Linked List

```python
first = DoublyListNode(1)
second = DoublyListNode(2)
third = DoublyListNode(3)

first.next = second

second.prev = first
second.next = third

third.prev = second
```



Why LL Playground?
Linked-list problems in Python often require a surprising amount of repetitive setup.
Before you can work on the algorithm itself, you need to define the ListNode Class and manually define a linked list.
LL Playground handles that surrounding work so you can focus on the linked-list logic itself.
Supported Structures
Singly Linked Lists
1 -> 2 -> 3 -> 4 -> None

Doubly Linked Lists
None <- 1 <-> 2 <-> 3 <-> 4 -> None

Requirements
Python 3.8+
Development
Clone the repository:
git clone https://github.com/BL4Z23/LL-Playground

cd LL-Playground
Status
LL Playground is currently in early development. The API may evolve as new utilities and linked-list features are added.
License
Licensed under the MIT License.


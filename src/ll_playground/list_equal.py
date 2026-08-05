from .printer import linked_to_list, validate_dll_links

def lists_equal(head1, head2):
    return linked_to_list(head1) == linked_to_list(head2)


def dlists_equal(head1, head2):
    if not (validate_dll_links(head1) and validate_dll_links(head2)):
        return False
    return linked_to_list(head1) == linked_to_list(head2)

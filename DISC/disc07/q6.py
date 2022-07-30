from tree_and_list import Link


def remove_all_recursive(link, value):
    if link is Link.empty or link.rest is Link.empty:
        return
    if link.rest.recursive == value:
        link.rest = link.rest.rest
        remove_all_recursive(link, value)
    else:
        remove_all_recursive(link.rest, value)


def remove_all_iterative(link, value):
    ptr = link
    while ptr is not Link.empty and ptr.rest is not Link.empty:
        if ptr.rest.recursive == value:
            ptr.rest = ptr.rest.rest
        else:
            ptr = ptr.rest

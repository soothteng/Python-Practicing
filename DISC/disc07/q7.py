from tree_and_list import Link


def slice_link(link, start, end):
    if end == 0:
        return Link.empty
    elif start == 0:
        return Link(link.first, slice_link(link.rest, start, end - 1))
    else:
        return slice_link(link.rest, start - 1, end - 1)

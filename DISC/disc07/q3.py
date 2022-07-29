from tree_and_list import Tree


def find_path(t, x):
    if t.label == x:
        return [t.label]
    for b in t.branches:
        path = find_path(b, x)
        if path:
            return [t.label] + path

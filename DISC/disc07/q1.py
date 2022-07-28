from tree_and_list import tree, link


def height(t):
    if t.is_leaf():
        return 0
    else:
        return 1 + max([height(b) for b in t.branches])

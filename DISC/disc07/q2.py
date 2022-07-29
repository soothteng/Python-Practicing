from tree_and_list import Tree


def max_path_sum(t):
    if t.is_leaf():
        return t.label
    else:
        return t.label + max([max_path_sum(b) for b in t.branches])

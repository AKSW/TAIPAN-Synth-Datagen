"""TreeWalker contains functions for walking a tree. :)"""


def build_permutation_tree(tree):
    """
    Build permutation tree.

    Given list [1,2,1] it will produce output such as:
    [0,0,0]
    [0,0,1]
    [0,1,0]
    [0,1,1]
    ...
    [1,2,1]

    Suboptimal. Memory explodes at one point.
    """
    permutations = []
    initial_value = [0] * len(tree)
    r_edges_length_list = list(reversed(tree))
    index = 0
    while True:
        if initial_value[index] < r_edges_length_list[index]:
            if index == 0:
                initial_value[index] += 1
            else:
                initial_value[index] += 1
                for reset in range(0, index):
                    initial_value[reset] = 0
                index = 0
            permutations.append(list(reversed(initial_value)))

        if initial_value[index] >= r_edges_length_list[index]:
            index += 1

        if initial_value == r_edges_length_list:
            break

    return permutations


def sort_permutation_tree(permutations):
    """
    Sort permutation tree.

    Sorting by sum of all elements.
    This is required function for build_permutation_tree
    """
    return sorted(permutations, key=lambda x: sum(x))


def walk_tree(tree):
    pass


def distribute_weight(weight, number_of_buckets):
    if weight == 0 and number_of_buckets == 0:
        raise Exception("number of buckets can not be 0")

    i = weight
    j = 0
    while i:
        zero_tuple = (0,) * number_of_buckets

        i = i - 1
        j = j + 1

def number_to_sum(number, sum_length):
    pass

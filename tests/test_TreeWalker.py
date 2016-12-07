"""Test methods from TreeWalker package."""

import opentablebench.TreeWalker as tw

import pytest


@pytest.fixture
def example_list():
    """Load example list to permutate."""
    return [1, 2, 4]


@pytest.fixture
def example_list_big():
    """Load example list to permutate."""
    return [10, 20, 40, 15, 64, 21, 33, 84, 10, 65]


def test_build_permutation_tree(example_list):
    """Test build_permutation_tree method."""
    permutations = tw.build_permutation_tree(example_list)
    assert len(permutations) == 29


@pytest.mark.skip(reason="Overflows RAM")
def test_build_permutation_tree_big(example_list_big):
    """Test build_permutation_tree method."""
    permutations = tw.build_permutation_tree(example_list_big)
    # does not matter as this will never execute
    assert len(permutations) > 0


def test_sort_permutation_tree():
    """Test sort_permutation_tree method."""
    _list = [1, 2, 1]
    permutations = tw.build_permutation_tree(_list)
    sorted_permutations = tw.sort_permutation_tree(permutations)
    result = [[0, 0, 1],
              [0, 1, 0],
              [1, 0, 0],
              [0, 1, 1],
              [0, 2, 0],
              [1, 0, 1],
              [1, 1, 0],
              [0, 2, 1],
              [1, 1, 1],
              [1, 2, 0],
              [1, 2, 1]]
    assert result == sorted_permutations


def test_walk_tree(example_list):
    pass


def test_distribute_weight():
    weight = 0
    number_of_buckets = 3
    distribution = tw.distribute_weight(weight, number_of_buckets)
    assert distribution == [(0, 0, 0)]

    weight = 1
    number_of_buckets = 3
    distribution = tw.distribute_weight(weight, number_of_buckets)
    assert distribution == (0, 0, 0)


def test_distribute_weight_zero():
    weight = 0
    number_of_buckets = 0
    with pytest.raises(Exception):
        tw.distribute_weight(weight, number_of_buckets)

def test_number_to_sum():
    number = 0
    sum_length = 1
    assert [(0)] == tw.number_to_sum(number, sum_length)
    sum_length = 2
    assert [(0,0)] == tw.number_to_sum(number, sum_length)
    number = 3
    sum_length = 4
    assert [
        (3,0,0,0),
        (2,1,0,0),
        (1,1,1,0)] == tw.number_to_sum(number, sum_length)
    number = 5
    sum_length = 4
    assert [
        (5,0,0,0),
        (4,1,0,0),
        (3,2,0,0),
        (3,1,1,0),
        (2,2,1,0),
        (2,1,1,1)] == tw.number_to_sum(number, sum_length)
    number = 8
    sum_length = 5
    assert [
        (8,0,0,0,0),
        (7,1,0,0,0),
        (6,2,0,0,0),
        (6,1,1,0,0),
        (5,2,1,0,0),
        (5,1,1,1,0),
        (4,3,1,0,0),
        (4,2,2,0,0),
        (4,2,1,1,0),
        (4,1,1,1,1),
        (3,2,1,1,1),
        (2,2,2,1,1),
        ] == tw.number_to_sum(number, sum_length)

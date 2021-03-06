"""
Solution of;
Project: Problems vs Algorithms
Problem 4: Dutch National Flag Problem
"""


def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """

    # if input_list is empty
    if input_list == []:
        return "list is not valid!"

    zeros = []
    ones = []
    twos = []
    result = []

    # iterate for items
    for item in input_list:

        if item == 0:
            zeros.append(0)

        elif item == 1:
            ones.append(1)

        else:
            twos.append(2)

    result += zeros
    result += ones
    result += twos

    return result


def test_function(test_case):
    if test_case == []:
        print([])
        print("Pass")
        return
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2,
               2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])

test_function([])

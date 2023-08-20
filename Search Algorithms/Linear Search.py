from typing import List


# Function for linear search to find the index of a target value (singular occurrence).
def linear_search(search_list: List, target_value):
    """
    Perform linear search to find the index of a target value in the list.

    Parameters:
        search_list (list): The list in which to search for the target value.
        target_value: The value to be searched for.

    Returns:
        int: The index of the target value.

    Raises:
        ValueError: If the target value is not in the list.
    """
    for idx in range(len(search_list)):
        if search_list[idx] == target_value:
            return idx
    raise ValueError("{0} not in list".format(target_value))


# Function for linear search to find all indices of a target value (multiple occurrences).
def linear_search_multiple(search_list: List, target_value):
    """
    Perform linear search to find all indices of a target value in the list (multiple occurrences).

    Parameters:
        search_list (list): The list in which to search for the target value.
        target_value: The value to be searched for.

    Returns:
        list: A list of indices where the target value is found.

    Raises:
        ValueError: If the target value is not in the list.
    """
    matches = []
    for idx in range(len(search_list)):
        if search_list[idx] == target_value:
            matches.append(idx)
    if matches:
        return matches
    else:
        raise ValueError("{0} not in list".format(target_value))


# Function for linear search to find the index of the maximum value.
def linear_search_max(search_list: List):
    """
    Perform linear search to find the index of the maximum value in the list.

    Parameters:
        search_list (list): The list in which to find the maximum value.

    Returns:
        int: The index of the maximum value.
    """
    maximum_score_index = None
    for idx in range(len(search_list)):
        if not maximum_score_index or search_list[idx] > search_list[maximum_score_index]:
            maximum_score_index = idx
    return maximum_score_index

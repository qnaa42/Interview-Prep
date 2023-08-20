def binary_search(sorted_list, left_pointer, right_pointer, target):
    """
    Perform binary search to find the index of a target value in a sorted list.

    Parameters:
        sorted_list (list): The sorted list in which to search for the target value.
        left_pointer (int): The left pointer indicating the starting index of the sub-list.
        right_pointer (int): The right pointer indicating the ending index of the sub-list.
        target: The value to be searched for.

    Returns:
        int or str: The index of the target value if found, or "value not found" if not found.
    """
    # This condition indicates we've reached an empty "sub-list"
    if left_pointer >= right_pointer:
        return "value not found"

    # Calculate the middle index from the pointers now
    mid_idx = (left_pointer + right_pointer) // 2
    mid_val = sorted_list[mid_idx]

    if mid_val == target:
        return mid_idx
    if mid_val > target:
        # We reduce the sub-list by passing in a new right_pointer
        return binary_search(sorted_list, left_pointer, mid_idx, target)
    if mid_val < target:
        # We reduce the sub-list by passing in a new left_pointer
        return binary_search(sorted_list, mid_idx + 1, right_pointer, target)


#iteartive binary search
def binary_search_iterative(sorted_list, target):
    left_pointer = 0
    right_pointer = len(sorted_list)
    """
    Perform binary search to find the index of a target value in a sorted list.

    Parameters:
        sorted_list (list): The sorted list in which to search for the target value.
        left_pointer (int): The left pointer indicating the starting index of the sub-list.
        right_pointer (int): The right pointer indicating the ending index of the sub-list.
        target: The value to be searched for.

    Returns:
        int or str: The index of the target value if found, or "value not found" if not found.
    """
    while left_pointer < right_pointer:
        mid_idx = (left_pointer + right_pointer) // 2
        mid_val = sorted_list[mid_idx]
        if mid_val == target:
            return mid_idx
        if target < mid_val:
            # we reduce the sub-list by passing in a new right_pointer
            right_pointer = mid_idx
        if target > mid_val:
            # we reduce the sub-list by passing in a new left_pointer
            left_pointer = mid_idx + 1
    return "value not found"

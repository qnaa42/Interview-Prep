class Node:
    def __init__(self, value, next_node=None):
        # Constructor to initialize a Node instance.
        # Parameters:
        #   - value: The value to be stored in the node.
        #   - next_node: The next node in the linked list (default is None).
        self.value = value
        self.next_node = next_node

    def set_next_node(self, next_node):
        # Method to set the next node of the current node.
        # Parameters:
        #   - next_node: The node to be set as the next node.
        # Note: This method violates immutability, as it allows changing the next node.
        self.next_node = next_node

    def get_next_node(self):
        # Method to retrieve the next node of the current node.
        # Returns:
        #   - The next node in the linked list.
        return self.next_node

    def get_value(self):
        # Method to retrieve the value stored in the node.
        # Returns:
        #   - The value stored in the node.
        return self.value
import Node

class LinkedList:
    def __init__(self, value=None):
        # Constructor to initialize a linked list with an optional initial value.
        # Parameters:
        #   - value: The value for the initial node (default is None).
        self.head_node = Node(value)

    def get_head_node(self):
        # Method to retrieve the head node of the linked list.
        # Returns:
        #   - The head node of the linked list.
        return self.head_node

    def insert_beginning(self, new_value):
        # Method to insert a new node at the beginning of the linked list.
        # Parameters:
        #   - new_value: The value for the new node.
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node

    def stringify_list(self):
        # Method to create a string representation of the linked list's values.
        # Returns:
        #   - A string containing the values of the linked list nodes.
        string_list = ""
        current_node = self.get_head_node()
        while current_node:
            if current_node.get_value() is not None:
                string_list += str(current_node.get_value()) + "\n"
            current_node = current_node.get_next_node()
        return string_list

    def remove_node(self, value_to_remove):
        # Method to remove a node with a specific value from the linked list.
        # Parameters:
        #   - value_to_remove: The value to be removed from the linked list.
        current_node = self.get_head_node()
        if current_node.get_value() == value_to_remove:
            self.head_node = current_node.get_next_node()
        else:
            while current_node:
                next_node = current_node.get_next_node()
                if next_node.get_value() == value_to_remove:
                    current_node.set_next_node(next_node.get_next_node())
                    current_node = None
                else:
                    current_node = next_node
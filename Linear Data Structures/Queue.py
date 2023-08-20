import Node.Node as Node


class Queue:
    def __init__(self, max_size=None):
        """
        Constructor to initialize a Queue instance.

        Parameters:
            max_size (int or None): The maximum size limit of the queue (default is None, no limit).
        """
        self.head = None
        self.tail = None
        self.max_size = max_size
        self.size = 0

    def enqueue(self, value):
        """
        Add an element to the end of the queue (enqueue operation).

        Parameters:
            value: The value to be added to the queue.
        """
        if self.has_space():
            item_to_add = Node(value)
            print("Adding " + str(item_to_add.get_value()) + " to the queue!")
            if self.is_empty():
                self.head = item_to_add
                self.tail = item_to_add
            else:
                self.tail.set_next_node(item_to_add)
                self.tail = item_to_add
            self.size += 1
        else:
            print("Sorry, no more room!")

    def dequeue(self):
        """
        Remove and return the element from the front of the queue (dequeue operation).

        Returns:
            The value of the element removed from the queue.
        """
        if self.get_size() > 0:
            item_to_remove = self.head
            print(str(item_to_remove.get_value()) + " is served!")
            if self.get_size() == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.get_next_node()
            self.size -= 1
            return item_to_remove.get_value()
        else:
            print("The queue is totally empty!")

    def peek(self):
        """
        Get the value of the element at the front of the queue without removing it.

        Returns:
            The value of the element at the front of the queue.
        """
        if self.size > 0:
            return self.head.get_value()
        else:
            print("No orders waiting!")

    def get_size(self):
        """
        Get the current size of the queue.

        Returns:
            The size of the queue.
        """
        return self.size

    def has_space(self):
        """
        Check if there is space available in the queue.

        Returns:
            bool: True if space is available, False otherwise.
        """
        if self.max_size is None:
            return True
        else:
            return self.max_size > self.get_size()

    def is_empty(self):
        """
        Check if the queue is empty.

        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return self.size == 0

from __future__ import annotations


class Lifo:
    """
    This is an implementation of the Lifo (last in, first out) data structure, based on python's list
    (https://docs.python.org/3.7/tutorial/datastructures.html#using-lists-as-stacks).
    """
    def __init__(self, elements: list | None = None):
        """
        Initialise the underlying container with a predefined list of elements.
        The elements' list will be copied to the underlying container.
        If the list of elements is None (default), an empty list will be created.
        :param elements: List of elements
        """
        if elements is None:
            elements = list()

        assert isinstance(elements, list) is True, f"Expected parameter 'elements' to of type 'list', " \
                                                   f"got {type(elements)}"
        self._elements = elements.copy()

    def container(self) -> list:
        """
        Returns the underlying container (list).
        :return: The underlying container.
        """
        return self._elements

    def size(self) -> int:
        """
        Returns the number of elements in the Lifo.
        :return:The number of elements in the underlying container.
        """
        return len(self._elements)

    def empty(self) -> bool:
        """
        Returns whether the Lifo is empty: i.e. whether its size is zero.
        :return: True if the underlying container's size is 0, False otherwise.
        """
        if self.size() > 0:
            return False
        else:
            return True

    def clear(self) -> None:
        """
        Remove all items from the underlying container.
        :return: None.
        """
        self._elements.clear()

    def front(self) -> object | None:
        """
        Returns the next element in the Lifo.
        The next element is the "newest" element in the Lifo and the same element
        that is popped out from the Lifo when Lifo.pop is called.
        :return: The next element in the Lifo if it's not empty. None otherwise.
        """
        if self.empty() is False:
            return self._elements[-1]
        else:
            return None

    def back(self) -> object | None:
        """
        Returns the last element in the Lifo.
        This is the "oldest" element in the Lifo (i.e. the first element pushed into the Lifo).
        :return: The last element in the Lifo if it's not empty. None otherwise.
        """
        if self.empty() is False:
            return self._elements[0]
        else:
            return None

    def push(self, element: object) -> None:
        """
        Inserts a new element at the end of the Lifo.
        :param element: element to be inserted.
        :return: None.
        """
        self._elements.append(element)

    def pop(self) -> object | None:
        """
        Removes the next element in the Lifo, effectively reducing its size by one.
        The element removed is the "newest" element in the Lifo which can be retrieved
        by calling member Lifo.front.
        :return: The next element in the Lifo if it's not empty. None otherwise.
        """
        if self.empty() is False:
            return self._elements.pop()
        else:
            return None

    def __str__(self):
        """
        Returns the underlying container as a string.
        :return: The underlying container string.
        """
        return str(self._elements)

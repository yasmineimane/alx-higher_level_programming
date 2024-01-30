#!/usr/bin/python3
"""Defines a classes fpr a singly_linked list"""


class Node:
    """Represents a noode in a singly linked list"""

    def __init__(self, data, next_node=None):
        """Initialize a new node.
        Args:
            data(int): tha data of the new node.
            next_node(Node): the next node of the new node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get/Set the data for the new node."""
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get/Set the next_node of the Node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if type(value) is not Node and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represents a singly linked list"""

    def __init__(self):
        """Initialize a new singly linked list"""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new Node to the singlyLinkedList.
        Args:
            value(int): the new node to be inseterd.
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """Defines the print representation of a singlylinkedlist"""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))

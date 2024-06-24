
"""Implements a Bloom filter class.

Note:
    This filter has been implemented such that is can be use
    in two different ways.
    - by specify the capacity and the false positive rate
    - by parsing in the bit array size and the number of hash functions

    For case 1, the optimal bit array size and the optimal number
    of hash functions are then computed programmtically.

"""

import math
import mmh3


class BloomFilter:

    def __init__(self, capacity: int, fpr: float,
                 m: int = 0, k: int = 0) -> None:
        """Initialize the bloom filter.

        Args:
            capcacity (int): Number of elements the filter can hold
            fpr (float):  The false positive rate
            m (int): The bit array size
            k (int): Number of hash functions to use

        Returns:
            None.
        """

        self.capacity = capacity  # Define the filter capacity
        self.fpr = fpr  # False positive rate
        self.m = m  # Bit array size
        self.k = k  # Number of hash functions
        self.bit_array = [False] * self.m  # Set all cells to False

    @property
    def m(self):
        """Get the value of the m.

        Returns:
            int: The current value of the bit array size.
        """
        return self.__m

    @m.setter
    def m(self, m):
        """Set the value of the m.

        Note: If the input value is not provided, it calculates
        the bit array size. It also checks if the provided value
        is valid.

        Args:
            m (int): The bit array size to be set.

        Raises:
            ValueError: If the provided value is negative.
        """
        if not m:
            m = self.calculate_bit_array_size()
        if m < 0:
            raise ValueError("m should be positive")
        self.__m = m

    @property
    def k(self):
        """Get the value of the k.

        Returns:
            int: The current value of the number of hash functions.
        """
        return self.__k

    @k.setter
    def k(self, k):
        """Set the value of the k.

        Note: If the input value is not provided, it calculates the
        optimal number of hash functions. It also checks if the
        provided value is valid.

        Args:
            k (int): The number of hash functions to be set.

        Raises:
            ValueError: If the provided value is negative.
        """
        if not k:
            k = self.optimal_hash_functions()
        if k < 0:
            raise ValueError("k should be positive")
        self.__k = k

    @property
    def capacity(self):
        """
        Get the value of the private attribute __capacity.

        Returns:
            int: The current value of the capacity.
        """
        return self.__capacity

    @capacity.setter
    def capacity(self, capacity):
        """Set the value of the capacity and check for its validity.

        Args:
            capacity (int): The capacity to be set.

        Raises:
            ValueError: If the provided value is not positive.
        """
        if capacity <= 0:
            raise ValueError("Capacity should be positive")
        self.__capacity = capacity

    @property
    def fpr(self):
        """
        Get the value of the private attribute __fpr (false positive rate).

        Returns:
            float: The current value of the false positive rate.
        """
        return self.__fpr

    @fpr.setter
    def fpr(self, fpr):
        """Set the value of the fpr (false positive rate) and check validity.

        Args:
            fpr (float): The false positive rate to be set. It should be
                between 0 and 1 inclusive.

        Raises:
            ValueError: If the provided value is not between 0 and 1 inclusive.
        """
        if not (0 <= fpr <= 1):
            raise ValueError("False positive rate should be between 0 and 1")
        self.__fpr = fpr

    def insert(self, element: str):
        """Adds an element to the filter.

        Args:
            element (str): The element to hash

        Returns:
            None. Sets several bits to True
        """
        indices = []
        for i in range(1, self.k + 1):
            index = self.hash_function(element, i) % self.m
            self.bit_array[index] = True
            indices.append(index)
        return indices

    def check(self, element: str):
        """Checks if an element exists in the filter.

        Args:
            element (str): The element to be checked in the bloom filter.

        Returns:
            bool: True if the element is probably in the filter, False if
                the element is definitely not in the filter.
        """
        for i in range(1, self.k + 1):
            index = self.hash_function(element, i) % self.m
            if not self.bit_array[index]:
                return False
        return True

    def __contains__(self, element: str) -> bool:
        """Allows usage of 'in' keyword to check membership.

        Args:
            element (str): The element to be checked.

        Returns:
            bool: True if the element is probably in the filter,
                False otherwise.
        """
        return self.check(element)

    @staticmethod
    def hash_function(element: str, seed: int) -> int:
        """
        Apply a hash function to an element.

        Args:
            element (str): The element to hash.
            seed (int): The seed for the hash function.

        Returns:
            An integer representing the hash value.
        """
        return mmh3.hash(element, seed)

    def calculate_bit_array_size(self):
        """Calculates the optimal bit array size for the filter.

        Args:
            capcacity (int): Number of elements the filter can hold
            false_positive_rate (float): User defined accepatble value
                for false positive rate

        Returns:
            An integer representing the size of the bit array calculated
                with the function.
        """
        size_of_bit = int(-(self.capacity * math.log(self.fpr)) /
                          (math.log(2) ** 2))
        return size_of_bit

    def optimal_hash_functions(self):
        """Calculates the optimal number of hash functions for the filter.

        Args:
            size_of_bit (int):
            capacity (int): Number of elements the filter can hold

        Returns:
            An integer representing the optimal number of hash functions
                to calculate the hash value.
        """
        no_of_hash_functions = math.ceil((self.m /
                                          self.capacity) * math.log(2))
        return no_of_hash_functions

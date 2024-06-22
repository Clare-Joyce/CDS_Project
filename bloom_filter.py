import math
import mmh3


class BloomFilter:

    def __init__(self, capacity: int, fpr: float,
                 m: int = 0, k: int = 0) -> None:
        """Initialize the bloom filter.

        Args:
            capcacity (int): Number of elements the filter can hold
            num_hash_functions (int): Number of hash functions to use

        Returns:
            None.
        """
        # Define the filter capacity
        self.capacity = capacity
        self.fpr = fpr
        self.m = m
        self.k = k
        # Set all cells to False
        self.bit_array = [False] * self.m

    @property
    def m(self):
        return self.__m

    @m.setter
    def m(self, m):
        if not m:
            m = self.calculate_bit_array_size()
        if m < 0:
            raise ValueError("m should be positive")
        self.__m = m

    @property
    def k(self):
        return self.__k

    @k.setter
    def k(self, k):
        if not k:
            k = self.optimal_hash_functions()
        if k < 0:
            raise ValueError("k should be positive")
        self.__k = k

    def insert(self, element: str):
        """Adds an element to the filter.

        Args:
            element (str): The element to hash

        Returns:
            None. Sets several bits to True
        """
        indices = []
        for i in range(self.k):
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
        for i in range(self.k):
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
        no_of_hash_functions = int((self.fpr) * math.log(2))
        return no_of_hash_functions

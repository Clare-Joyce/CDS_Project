from typing import Any
import math


class BloomFilter:

    def __init__(self, capacity: int, false_positive_rate: float) -> None:
        """Initialize the bloom filter.

        Args:
            capcacity (int): Number of elements the filter can hold
            num_hash_functions (int): Number of hash functions to use

        Returns:
            None.
        """
        # Define the filter capacity
        self.capacity = capacity
        self.false_positive_rate = false_positive_rate
        # Set all cells to False
        self.bit_array = [False]  * capacity


    def insert(self, item):
        """Adds an element to the filter."""
        pass


    def check(self):
        """Checks if an element exists in the filter."""
        pass


    def hash_function(self):
        pass


    @staticmethod
    def calculate_bit_array_size(capacity, false_positive_rate):
        """Calculates the optimal bit array size for the filter."""
        size_of_bit = int(-(capacity * math.log(false_positive_rate)) / (math.log(2) ** 2))
        return size_of_bit

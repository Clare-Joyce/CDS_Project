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
        """Calculates the optimal bit array size for the filter.

        Args:
            capcacity (int): Number of elements the filter can hold
            false_positive_rate (float): User defined accepatble value 
                for false positive rate

        Returns:
            An integer representing the size of the bit array calculated with the function.   
        """
        size_of_bit = int(-(capacity * math.log(false_positive_rate)) / (math.log(2) ** 2))
        return size_of_bit

    @staticmethod
    def optimal_hash_functions(size_of_bit, capacity):
        """Calculates the optimal number of hash functions for the filter.

        Args:
            size_of_bit (int): 
            capacity (int): Number of elements the filter can hold
        
        Returns:
            An integer representing the optimal number of hash functions 
                to calculate the hash value.
        """
        no_of_hash_functions = int((size_of_bit/capacity) * math.log(2))
        return no_of_hash_functions
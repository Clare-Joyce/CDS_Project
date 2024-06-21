from typing import Any
import math
import mmh3


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
        self.bit_array_size = self.calculate_bit_array_size(capacity, false_positive_rate)
        self.num_hash_functions = self.optimal_hash_functions(capacity, false_positive_rate)
        # Set all cells to False
        self.bit_array = [False]  * self.bit_array_size


    def insert(self, element: Any):
        """Adds an element to the filter."""
        for i in range(self.num_hash_functions):
            index = self.hash_function(element, i) % self.bit_array_size
            self.bit_array[index] = True


    def check(self):
        """Checks if an element exists in the filter."""
        pass


    def hash_function(self, element: str, seed: int) -> int:
        """
        Apply a hash function to an element.
        
        Args:
            item (str): The item to hash.
            seed (int): The seed for the hash function.
        
        Returns:
            int: The hash value.
        """
        return mmh3.hash(element, seed)


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
    def optimal_hash_functions(capacity, false_positive_rate):
        """Calculates the optimal number of hash functions for the filter.

        Args:
            size_of_bit (int): 
            capacity (int): Number of elements the filter can hold
        
        Returns:
            An integer representing the optimal number of hash functions 
                to calculate the hash value.
        """
        bit_array_size = BloomFilter.calculate_bit_array_size(capacity, false_positive_rate)
        no_of_hash_functions = int((bit_array_size/capacity) * math.log(2))
        return no_of_hash_functions
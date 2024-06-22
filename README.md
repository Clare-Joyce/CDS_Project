# CDS_Project
Concepts of Data Science Course Project


## Bloom Filter Implementation

A Python implementation of a Bloom filter with a focus on space and time complexity, as well as accuracy benchmarking. In this project, we seek to understand probabilistic data structures, specifically exploring the Bloom filter. 

### Project Scope:

This project aims to implement a Bloom filter using Python, employing an object-oriented approach to facilitate clarity and reusability of code. Here's what the project will cover:

**Bloom Filter Basics:** We'll start by exploring the fundamental concepts behind Bloom filters, understanding how they work, and their key characteristics such as false positive probability and optimal hash functions.

**Python Implementation:** Using the object-oriented approach, we'll design and implement a Bloom filter class in Python. This will involve defining methods for adding elements to the filter, checking for membership, and optimizing memory usage.

**Benchmarking:** One of the primary objectives of this project is to evaluate the performance of our Bloom filter implementation. We'll conduct benchmarking experiments to analyze the space and time complexity of operations such as insertion and membership testing. Additionally, we'll assess the accuracy of our implementation by measuring false positive rates under various scenarios.


## Bloom Filter Basics

A bloom filter is a space-efficient probabilistic data structure used for checking if an element exist in a set. Its functionality is build on the trade off between accuracy and memory use. An ideal use case would be  one that tolerate some false positives but no false negatives. The outcome is either a firm no or a probable yes. A false positive happens when the element is not in the set and the filter says it is and a false negative which is NOT possible describes a situation where the element is there but the filter says it is not.

## Understanding How Bloom Filters Work

Imagine if we have several elements and we want to store the elements into a set meaning that no two are the same. A Bloom filter is a space-efficient probabilistic data structure used to test whether an element is a member of a set. An empty bloom filter is a bit array of specified bit length all set to zero when the bloom filter is initialized. Bloom filter works based on the hash function. For each element hash function calculates a unique hash value defined using the optimal number of hash functions which is considered as its identifier.

# Adding an item to the bloom filter

1. The element is hashed through optimal number of hash function
2. The hash value is generated from hash function and is reduced as per the length of bit array
3. Identify the position in bit array and set to 1.
There are chances that some bits on the bit array are set to one more than ones due to hash collisions.

# Checking if the element already exist

1. Element is hashed through the same hash functions
2. Identify the position in bit array which needs to be set to 1.
3. Verify if the positions are already set to 1 in the array
If any of the positions are set to zero we can make sure that the element is not present in the set, but if all possitions are already set to 1 that are high chances that the element is already a memeber of the set.

# False Positive Rate

While the bloom filter can guarantee that guarantee there is no false negatives that is when a filter says an element is not present, it is definitely not present, however they can produce false positives which means the filter says an element is present but it can be the case that it is not present. The false positive rate, can be computed using bit_array_size, no_of_hash_functions, and capacity which is the number of expected elements to be inserted into the filter.

# Calculations involved in the bloom filter

1. number of hash functions (no_of_hash_functions)
2. length of bit array (bit_array_size)
3. number of elements stored in the bloom filter (capacity)

# Properties of bloom filter

1. Time complexity : Quicker is the overall time of each process which is dependent on hash function used.
2. Independent : The hash functions are independent,  there is very less chance of more than one elements mapping to the same position in the bit array, this will reduce the possibility of false positives.
3. Uniform : Uniform distribution bits in the bit array reduces the chances of multiple elements hashing to the same bit positions which inturn reduce collision and false positive rate.

## Code Structure for the implementation

This section provides implementation steps in BloomFilter class with methods to add elements to the filter and check if it is already present in the set.

Class : BloomFilter
1. Initialization (__init__ method):
capacity : size of the bit array
fpr : false positive rate

2. Setter Method (@m.setter):
To calculate the size of the bit array.

3. Setter Method (@k.setter):
To calculate the optimal number of hash functions.

4. Setter Method (@capacity.setter):
To calculate the number of expected elements to be inserted in the bloom filter.

5. Setter Method (@fpr.setter):
To calculate the false positive rate.

6. Insert function (insert method)
It adds an element to the filter.

7. Check function (check method)
It Checks if a new element before adding if it exists in the filter already.

8. Contains Method (__contains__ method)
Allows usage of 'in' keyword to check membership of an element in the bloom filter by means of hash values.

9. Hash function (hash_function static method)
This function calculates the hash values for each elements added to the bloom filter with its corresponding optimal number of hash functions and size of the bit array.

10. Size of bit array (calculate_bit_array_size static method)
This function calculate the bit array size, by computing the 'capacity' which is the number of elements the filter can hold.

11. Optimal number of hash function (optimal_hash_functions static method)
This function calculates the optimal number of has functions to be calculated for each element which is added to the filter.


**suggested code structure**
CDS_Project:
    bloom_filter.py: what it does
    report.ipynd: what it contains
    .
    .
    .
    .

## Tests

In order to test the implementation performance of the bloom filters with two types of large dataset a set of random words and DNA sequences are generated with functions.

1. random_word_generator function
Generates a random set of words of a given length

2. generate_dna_sequence function
Generates a random DNA sequence of a given length



## Benchmarking


## Results

## Resources
* https://brilliant.org/wiki/bloom-filter/
* https://www.geeksforgeeks.org/bloom-filters-introduction-and-python-implementation/
* https://andybui01.github.io/bloom-filter/#implementation-and-benchmarks

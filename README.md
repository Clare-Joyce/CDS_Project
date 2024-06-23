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

Suppose we need to add an element 'github' to the bloom filter, we use a bit array of length 10, all set to 0 initially.

![alt text](https://github.com/Clare-Joyce/CDS_Project/blob/main/Figures/image_1.png)

Assume the optimal hash function is calculated to be 3 representing h1, h2, h3. The calculated has value corresponds to h1 = 1, h2 = 3 and h3 = 7. The bits at indices 1 , 2 and 7 are set to 1.

![alt text](https://github.com/Clare-Joyce/CDS_Project/blob/main/Figures/image_2.png)

Now we add a new element 'data' to the bloom filter. The calculated optimal hash functions are 3 and corresponding hash values as h1 = 2, h2 = 3 and h3 = 9. Similarly bits at indices 2, 3 and 9 are set to 1.

![alt text](https://github.com/Clare-Joyce/CDS_Project/blob/main/Figures/image_3.png)

# Checking if the element already exist

1. Element is hashed through the same hash functions
2. Identify the position in bit array which needs to be set to 1.
3. Verify if the positions are already set to 1 in the array
If any of the positions are set to zero we can make sure that the element is not present in the set, but if all possitions are already set to 1 that are high chances that the element is already a memeber of the set.

# False Positive Rate

While the bloom filter can guarantee that guarantee there is no false negatives that is when a filter says an element is not present, it is definitely not present, however they can produce false positives which means the filter says an element is present but it can be the case that it is not present. The false positive rate, can be computed using bit_array_size, no_of_hash_functions, and capacity which is the number of expected elements to be inserted into the filter.

Let us illustrate this with an example, Suppose we want to check if 'pen' is already present or not. The hash value calculated is h1 = 2, h2 = 3 and h3 = 7.

![alt text](https://github.com/Clare-Joyce/CDS_Project/blob/main/Figures/image_4.png)

Even if we know 'pen' was never added to the set, the indices 2 was previously added for 'data' and indices 3 and 7 was added for 'github'. So bloom filter claims that 'pen' is already added to the set, which indicates a false positive case.
By using a larger bit array size and more number of hash functions we can reduce the false positive rates.

# Calculations involved in the bloom filter

1. number of hash functions (no_of_hash_functions)

![alt text](https://github.com/Clare-Joyce/CDS_Project/blob/main/Figures/optimum_hash_function.png)

k - number of hash functions, m - size of bit array, n - number of elements to be inserted.

2. length of bit array (bit_array_size)

![alt text](https://github.com/Clare-Joyce/CDS_Project/blob/main/Figures/bit_array_size.png)

n - number of expected elements, p - false positive rate, m - bit array size.

3. false positive rate(fpr)

![alt text](https://github.com/Clare-Joyce/CDS_Project/blob/main/Figures/fpr_equation.png)

p - false positive rate, m - size of bit array, k - number of hash functions, n - number of expected elements.

# Time and Space Complexity

The bloom filter's time and space efficiency is a key benefit.  Ignorable value of accuracy is sacrificed maintain these features.

A bloom filter of m bits and k optimal number of hash functions, the time order for operations insertion and searching takes O(k) time. This is because the element as such is not entering the filter only the calculated hash values enters. Hence the time complexity does not depend on the number of elements already entered.

The space complexity involved in the bloom filter is O(m). This is evaluated by m which is the size of the bit array where the hash values for each elements are stored. The number of hash functions does not directly impact the space complexity. A larger value of m will reduce the false positive rate.

![alt text](https://github.com/Clare-Joyce/CDS_Project/blob/main/Figures/Time_Space_Complexity.png)

# Properties of bloom filter

1. Independent : The hash functions calculated for each elements are independent of each other,  due to this property there is very less chance of more than one elements mapping to the same position in the bit array. The independence reduces the correlation between the hash values this will inturn reduces the possibility of false positives.
2. Uniform : Uniform distribution of bits in the bit array reduces the chances of multiple elements hashing to the same bit positions. This will ensure the optimal utilization of space and improve the accuracy of membership queries, which inturn reduce collision and false positive rate.

## Code Structure for the implementation

This section provides the details on the code structure for the entire implementation of this project.


CDS_Project

    Figures : The folder containing all images (png) which are used in README.md file to illustrate the     functionality of bloom filter

    bloom_filter.py : The python file has the code of Class for Bloom filter, using mmh3 hash function.
        
    dna_sequence_generator.py : The python function to generate random DNA sequences of given length and count to test the functionality of bloom filter.
        
    independence_and_uniformity.py : The python function to evaluate the independence and uniformity properties of bloom filter.
        
    main.py : The main python programe which has the entry modeule to initialize the code, and calls to other functions and class to start the program logic.
        
    README.md : The mark down file which contains the content of project repository and implementation of the project.
        
    report.ipynb : The report created from the benchmarking process which has a comprehensive details about the functionality and performance of the bloom filter.
        
    word_generator.py : The python function to generate randon words of given count to test the functionality of bloom filter.

    test_bloom_filter.py : The python test script which contains sample test cases to test the basic functionality of bloom filter.
    
    jobscript.py : A job script with comments to automate the execution of tasks in high performance coputing (HPC).

## Example Run
This section illustrates how to use the filter
```python
from bloom_filter import BloomFilter


capacity = 100
false_positive_rate = 0.01
bloom_filter = BloomFilter(capacity, false_positive_rate, 100, 5)

elements_to_insert = ["apple", "banana", "orange"]
for element in elements_to_insert:
    bloom_filter.insert(element)

for element in elements_to_insert:
    if bloom_filter.check(element):
        print(f"Success: {element} is probably in the filter.")
    else:
        print(f"Error: {element} should be in the filter but is not detected.")

# OUTPUT
Success: apple is probably in the filter.
Success: banana is probably in the filter.
Success: orange is probably in the filter.

test_element_not_in_filter = "nonexistent"
if test_element_not_in_filter in bloom_filter:
    print(f"Warning: {test_element_not_in_filter} is not in the filter but was detected (false positive).")
else:
    print(f"{test_element_not_in_filter} is not in the filter (expected).")

# OUTPUT
nonexistent is not in the filter (expected).
```

The basic operation of the Bloom filter implementation was initially tested using `pytest' before starting with the benchmarking. This is ensure that the code is correct and that all operations does function as intended.

## Testing and Benchmarking

The basic operation of the Bloom filter implementation was initially tested as illustrated above before starting with the benchmarking. This is to ensure that the code is correct and that all operations do function as intended.

Though the filter is implemented with take both words and DNA sequences, it was tested only with random words generated with functions.


[Benchmarking](report.ipynb)


## Results

The functionality on implementation of bloom filter was tested throughly and benchmarked. The testing ensured the basic operations such as insertion and searching works as expected with calculation of optimal number of hash functions by ensuring the minimal false positive rate. The benchmarking allowed to evaluate the efficiency of bloom filter while working with larage scale data sets. The insertion time, checking time and false positive rates were evaluated for increasing input size and increasing number of hash functions. The insertion time and search time showed a linear behaviour with increase in input sizes, indicating a consistent performance at various scales. With increase in hash functions the time insertion and checking time also increased which suggests the optimization required for cases where we have higher high insertion rates. When the optimal number of hash functions increases beyond a threshold level, the false positive rate increases initially and further stabilizes to a constant level. The benchmarking results affirms the scalability and efficiency of our bloom filter implementation in real world applications. However certain limitations like increased insertion time, checking time and false positive rates with increased number of hash functions should be optimized based on the application. The future improvements could be done on optimising the hash function computations and comparison with different variants of Bloom filters.

## Resources
* https://brilliant.org/wiki/bloom-filter/
* https://www.geeksforgeeks.org/bloom-filters-introduction-and-python-implementation/
* https://andybui01.github.io/bloom-filter/#implementation-and-benchmarks
* https://systemdesign.one/bloom-filters-explained


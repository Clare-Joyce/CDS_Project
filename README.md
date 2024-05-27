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


## Code Structure for the implementation


## Tests


## Benchmarking


## Results

## Resources
* https://brilliant.org/wiki/bloom-filter/ 
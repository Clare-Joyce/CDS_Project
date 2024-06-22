
"""

"""

from __future__ import annotations

from typing import List, Tuple
from bloom_filter import BloomFilter
from scipy.stats import chisquare
import numpy as np


def chi_square_test(bf: BloomFilter, elements: List[str],
                    alpha=0.05) -> Tuple:
    """
    Performs the test for uniformity and independence of a Bloom filter.

    Args:
        bf (BloomFilter): The Bloom filter to test.
        elements (List): The list of items to add to the Bloom filter.
        alpha (float): The significance level for the
            chi-square test.

    Returns:
        A tuple, 2 booleans indicating if the Bloom filter passes the
        uniformity and independence tests.
    """
    # Insert items into the Bloom filter and collect indices
    all_indices = []
    for element in elements:
        indices = bf.insert(element)
        all_indices.extend(indices)

    # Uniformity test
    bit_counts = [0] * bf.m
    for index in all_indices:
        bit_counts[index] += 1

    # Check uniformity
    expected_count = [1 / bf.m] * bf.m  # Equal probability of being set
    # Actual observed probability of each bit being set to 1
    freq = [f / len(all_indices) for f in bit_counts]
    _, p_value = chisquare(freq, expected_count)

    """
    When testing for uniformity in a Bloom filter, you aim
    to support the null hypothesis that the distribution
    of bits (1s) is uniform.
    """
    uniformity_passed = p_value > alpha

    # Independence test
    all_hashes = [[] for _ in range(bf.k)]
    for element in elements:
        indices = bf.insert(element)
        for i, index in enumerate(indices):
            all_hashes[i].append(index)

    squared_diff = 0
    for i in range(bf.k):
        for j in range(i + 1, bf.k):
            corr = np.corrcoef(all_hashes[i], all_hashes[j])[0, 1]
            squared_diff += corr ** 2
    independence_passed = (squared_diff /
                           (bf.k * (bf.k - 1) / 2) < alpha)

    return uniformity_passed, independence_passed

"""

"""

import argparse
import math
import time
import pandas as pd
from bloom_filter import BloomFilter
from dna_sequence_generator import generate_multiple_dna_sequences
from word_generator import random_word_generator

def parse_arguments():
    """Parses command line arguments."""
    parser = argparse.ArgumentParser(description="Bloom Filter Benchmarking Tool")
    parser.add_argument("--capacity", default=100, type=int, required=True,
                        help="Maximum number of elements the Bloom filter can hold.")
    parser.add_argument("--fpr", default=0.01, type=float, required=True,
                        help="Initial desired false positive rate.")
    parser.add_argument("--m", default=0, type=int, required=False,
                        help="Size of the bit array")
    parser.add_argument("--k", default=0, type=int, required=False,
                        help="Maximum number pf hash functions.")
    parser.add_argument("--data_type", type=str, choices=["words", "dna"],
                        required=True,
                        help="Type of data to use for benchmarking: 'words' or 'dna'.")
    parser.add_argument("--sequence_length", type=int, required=False,
                        help="Number of DNA sequences to generate.")

    return parser.parse_args()

def calculate_compression_rate(m: int, n: int) -> float:
    """
Calculate the compression rate of a Bloom filter.

    Args:
        m (int): Size of the bit array (number of bits).
        n (int): Number of elements inserted into the filter.

    Returns:
        A float,  the compression rate.
    """
    compression_rate = (m * math.log(2)) / n
    return compression_rate


def calculate_false_positive_rate(m: int, k: int, n: int) -> float:
    """
    Calculate the false positive rate of a Bloom filter.

    Args:
        m (int): Size of the bit array (number of bits).
        k (int): Number of hash functions.
        n (int): Number of elements inserted into the filter.

    Returns:
        A float,  False positive rate (probability).
    """
    # Calculate the probability of a single bit not being set by any of the hash functions
    prob_single_bit_not_set = math.exp(-(k * n) / m)

    # Calculate the probability of a single bit being set (at least one hash function sets the bit)
    prob_single_bit_set = 1 - prob_single_bit_not_set

    # Calculate the false positive rate
    false_positive_rate = prob_single_bit_set ** k

    return false_positive_rate

def process(cap, fpr, data_type, seq_len):
    """"""
    results = []
    for i in range(1, cap, 5):
        bf = BloomFilter(i, fpr)
        if data_type =="dna":
            items = generate_multiple_dna_sequences(i, seq_len)
        if data_type == "words":
            items = random_word_generator(i)
        start_time = time.time()
        for item in items:
            bf.insert(item)
        insertion_time = time.time() - start_time

        start_time = time.time()
        for item in items:
            bf.check(item)
        checking_time = time.time() - start_time

        fpr_new = calculate_false_positive_rate(bf.m, bf.k, i)
        cpr = calculate_compression_rate(bf.m, i)
        results.append((i, insertion_time, checking_time, fpr_new, cpr))
    df = pd.DataFrame(results, columns=["capacity", "insertion_time", "checking_time", "fpr", "cpr"])
    df.to_csv(f"dataframe_{data_type}_{cap}.csv")

    return df


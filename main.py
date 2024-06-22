"""

"""

import argparse
import math
import time
import pandas as pd
from bloom_filter import BloomFilter
from word_generator import random_word_generator
from dna_sequence_generator import generate_multiple_dna_sequences
from independence_and_uniformity import chi_square_test


def parse_arguments():
    """Parses command line arguments."""
    parser = argparse.ArgumentParser(
        description="Bloom Filter Benchmarking Tool")
    parser.add_argument("--capacity", default=100, type=int, required=False,
                        help="Maximum number of elements the filter can hold.")
    parser.add_argument("--fpr", default=0.01, type=float, required=False,
                        help="Initial desired false positive rate.")
    parser.add_argument("--m", default=0, type=int, required=False,
                        help="Size of the bit array")
    parser.add_argument("--k", default=0, type=int, required=False,
                        help="Maximum number pf hash functions.")
    parser.add_argument("--data_type", type=str, choices=["words", "dna"],
                        required=True,
                        help="Type of data to used: 'words' or 'dna'.")
    parser.add_argument("--sequence_length", type=int, required=False,
                        help="Number of DNA sequences to generate.")

    return parser.parse_args()


def calculate_compression_rate(m: int, n: int) -> float:
    """Calculate the compression rate of a Bloom filter.

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
    # Calculate the probability of a single bit not being set
    # by any of the hash functions
    prob_single_bit_not_set = math.exp(-(k * n) / m)

    # Calculate the probability of a single bit being set
    # (at least one hash function sets the bit)
    prob_single_bit_set = 1 - prob_single_bit_not_set

    # Calculate the false positive rate
    false_positive_rate = prob_single_bit_set ** k

    return false_positive_rate


def process() -> pd.DataFrame:
    """Processes bloom filter functionality and tests performance.

    Note:
        The bloom filter is designed to work in two ways. One could
        specify just the capacity and the false positive rate or
        specify the bit array size and the number of hash functions
        needed. For the first case, the program automatically calculates
        the optimal bit array size and the optimal number of hash functions.

    Args:
        cap (int): The initial capacity of the filter
        fpr (float): The false positive rate defined by the user
        m (int): The bit array size
        k (int): The desired number of hash functions
        data_type (str): The data type; normal words or DNA sequences
        seq_len (int): The length of the DNA sequence

    Returns:
        A pandas dataframe
    """

    args = parse_arguments()
    input_size = [i for i in range(10000, 1000001, 10000)]
    # input_size = [i for i in range(100, 1000, 100)]
    for k in range(5, args.k + 1, 5):
        results = []
        for i in input_size:
            bf = BloomFilter(args.capacity, args.fpr, args.m, k)
            if args.data_type == "dna":
                sl = args.sequence_length
                items_in = generate_multiple_dna_sequences(i, sl)
                items_check = generate_multiple_dna_sequences(i, sl)
            if args.data_type == "words":
                items_in = random_word_generator(i)
                items_check = random_word_generator(i)
            print(f"Inserting {i} words to the filter with {k} hash functions")
            start_time = time.time()
            for item in items_in:
                bf.insert(item)
            insertion_time = time.time() - start_time
            print(f"Checking {i} words in the filter with {k} hash functions")
            start_time = time.time()
            for item in items_check:
                bf.check(item)
            checking_time = time.time() - start_time

            fpr_new = calculate_false_positive_rate(bf.m, bf.k, i)
            cpr = calculate_compression_rate(bf.m, i)
            uniform, independent = chi_square_test(bf, items_in)
            results.append((i, insertion_time, checking_time, fpr_new,
                            cpr, uniform, independent))
        df = pd.DataFrame(results, columns=["input_size", "insertion_time",
                                            "checking_time", "fpr", "cpr",
                                            "uniform", "independent"])
        df.to_csv(f"dataframe_{args.data_type}_{k}.csv")

    return df


if __name__ == "__main__":
    process()

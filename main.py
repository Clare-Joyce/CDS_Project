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
                        help="Number pf hash functions.")
    parser.add_argument("--data_type", type=str, choices=["words", "dna"],
                        required=True,
                        help="Type of data to use for benchmarking: 'words' or 'dna'.")
    parser.add_argument("--sequence_length", type=int, required=False,
                        help="Number of DNA sequences to generate.")

    return parser.parse_args()

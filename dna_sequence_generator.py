"""Generates random DNA sequences."""

import random


def generate_dna_sequence(length: int) -> str:
    """Generates a random DNA sequence of a given length.

    Args:
        length (int): The length of the DNA sequence to generate.

    Returns:
        A string representing a random DNA sequence composed of 'A',
        'T', 'C', 'G'.
    """
    return ''.join(random.choice(['A', 'T', 'C', 'G']) for _ in range(length))


def generate_multiple_dna_sequences(num_sequences: int, length: int) -> list:
    """Generates several random DNA sequences.

    Args:
        num_sequences (int): Number of DNA sequences to generate.
        length (int): The length of each DNA sequence.

    Returns:
        list: A list of random DNA sequences.
    """
    return [generate_dna_sequence(length) for _ in range(num_sequences)]

"""Generates random words for testing."""
from faker import Faker

fake = Faker()


def random_word_generator(n):
    """Generates a random set of words.

    Args:
        n (int): The number of random uniform words to be generated.

    Returns:
        random_words (list): Returns a list of random words
    """
    random_words = [fake.word() for _ in range(n)]
    return random_words

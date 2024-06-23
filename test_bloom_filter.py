from pytest import mark
from bloom_filter import BloomFilter
from word_generator import random_word_generator


@mark.parametrize(
        "inputs, expected",
        [
            (["apple", "banana", "orange"], True),
            (random_word_generator(50), True),
        ]
)
def test_insert_and_check(inputs, expected):
    bf = BloomFilter(10000, 0.01, 10000, 5)
    for e in inputs:
        bf.insert(e)

    assert all(e in bf for e in inputs) == expected


@mark.parametrize(
        "inputs, expected",
        [
            (["apple", "banana", "orange"], True),
        ]
)
def test_elements_not_in_filter(inputs, expected):
    bf = BloomFilter(10000, 0.01, 10000, 5)
    for w in random_word_generator(10):
        if w not in inputs:
            bf.insert(w)

    assert all(e not in bf for e in inputs) == expected

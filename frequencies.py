"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    for v in items:
        v = str(v)
    frequencies = dict.fromkeys(items, 0)
    for k, v in frequencies.items():
        frequencies[k] = items.count(v)
    return frequencies
